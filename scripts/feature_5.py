#!/usr/bin/env python3

import os
import sys
import typer
import petl as etl
from datetime import datetime, timedelta
from common import read_input, write_output
from rich.progress import Progress

app = typer.Typer()

@app.command()
def extract_feature_5(
    input: str = typer.Option(..., "--input", help="Input CSV file"),
    head: int = typer.Option(None, "--head", help="Number of rows to process"),
    output: str = typer.Option(..., "--output", help="Output CSV file"),
    window: int = typer.Option(300, "--window", help="Time window size in seconds"),
    start_time: str = typer.Option(None, "--start-time", help="Starting timestamp for time windows (e.g., '2005-05-23 21:00:00')")
):
    """
    Extract feature_5: Number of prefixes where AS path changes but the origin AS remains the same.
    """
    typer.echo(f"Reading input file: {input}")

    # Initialize progress bar
    with Progress() as progress:
        # Read the input file (treat all rows as data)
        read_task = progress.add_task("[cyan]Reading input file...", total=None)
        data = etl.fromcsv(input, delimiter='|', header=range(0,13))
        if head:
            data = etl.head(data, head)
        progress.update(read_task, completed=True)

        # Determine or parse the start time
        if start_time:
            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        else:
            typer.echo("Start time not provided; using earliest timestamp in the data.")
            earliest_timestamp = min(etl.values(data, 2))  # Assuming the 3rd column is the timestamp
            start_time = datetime.fromtimestamp(float(earliest_timestamp.split('.')[0]))
        typer.echo(f"Using start time: {start_time}")

        # Add parsed timestamp column
        typer.echo("Adding parsed timestamp column...")
        def parse_timestamp(row):
            raw_timestamp = row[2]  # Assuming column 2 contains the timestamp
            if raw_timestamp:
                try:
                    return datetime.fromtimestamp(float(raw_timestamp.split('.')[0]))
                except ValueError:
                    return None
            return None

        parse_task = progress.add_task("[cyan]Parsing timestamps...", total=None)
        data = etl.addfield(data, "parsed_timestamp", parse_timestamp)
        progress.update(parse_task, completed=True)

        # Filter rows with valid ANNOUNCEMENTS, prefixes, and AS paths
        typer.echo("Filtering ANNOUNCEMENT messages with valid prefixes and AS paths...")
        message_type_col = 1  # Message type column
        prefix_col = "9"        # Prefix column
        as_path_col = "11"      # AS Path column
        origin_as_col = "12"    # Origin AS column

        filter_task = progress.add_task("[cyan]Filtering rows...", total=None)
        data = etl.select(
            data,
            lambda row: (
                row["parsed_timestamp"] is not None and
                row[message_type_col] == "A" and  # Only process announcements
                row[prefix_col] and row[as_path_col] and row[origin_as_col]  # Prefix, AS Path, and Origin AS must exist
            )
        )
        progress.update(filter_task, completed=True)

        # Debugging: Show the first 5 rows after filtering
        typer.echo("First rows after filtering:")
        typer.echo(etl.look(data, 5))

        # Process rows to calculate feature_5
        typer.echo("Processing rows to calculate feature_5...")
        current_window = []
        result = []

        # Dictionary to track last observed AS paths per prefix
        prefix_tracker = {}

        process_task = progress.add_task("[cyan]Processing time windows...", total=None)
        for row in data.dicts():
            try:
                timestamp = row["parsed_timestamp"]
                prefix = row[prefix_col]
                as_path = row[as_path_col]
                origin_as = row[origin_as_col]
            except KeyError:
                typer.echo("   ")
                typer.echo(f"%% ERROR row len: {len(row)}")
                typer.echo(repr(row))
                typer.echo("-----------------")
                raise

            if not prefix or not as_path or not origin_as:
                continue

            # If this row is outside the current window, process the current window
            if timestamp >= start_time + timedelta(seconds=window):
                unique_changes = len(set(current_window))
                result.append({"feature_name": "as_path_change_count", "timestamp": start_time, "value": unique_changes})
                start_time += timedelta(seconds=window)
                current_window = []

            # Check for AS path changes while origin AS remains the same
            if prefix in prefix_tracker:
                last_as_path, last_origin_as = prefix_tracker[prefix]
                if as_path != last_as_path and origin_as == last_origin_as:
                    current_window.append(prefix)

            # Update the tracker
            prefix_tracker[prefix] = (as_path, origin_as)
            
        progress.update(process_task, completed=True)

        # Append the remaining data for the last time window
        if current_window:
            unique_changes = len(set(current_window))
            result.append({"feature_name": "as_path_change_count", "timestamp": start_time, "value": unique_changes})

        # Write the results to the output file
        typer.echo(f"Writing results to output file: {output}")
        result_table = etl.fromdicts(result)
        write_output(output, result_table)
        typer.echo("Feature extraction complete!")


if __name__ == "__main__":
    app()
