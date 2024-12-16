#!/usr/bin/env python3

import typer
import petl as etl
from datetime import datetime, timedelta
from common import read_input, write_output
from rich.progress import Progress

app = typer.Typer()

@app.command()
def extract_feature_3(
    input: str = typer.Option(..., "--input", help="Input CSV file"),
    head: int = typer.Option(None, "--head", help="Number of rows to process"),
    output: str = typer.Option(..., "--output", help="Output CSV file"),
    window: int = typer.Option(300, "--window", help="Time window size in seconds"),
    start_time: str = typer.Option(None, "--start-time", help="Starting timestamp for time windows (e.g., '2024-12-12 00:00:00')")
):
    """
    Extract feature_3: Average AS path length for BGP update messages per time window.
    """
    typer.echo(f"Reading input file: {input}")

    # Initialize progress bar
    with Progress() as progress:
        # Read the input file
        read_task = progress.add_task("[cyan]Reading input file...", total=None)
        data = etl.fromcsv(input, delimiter='|')
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
            raw_timestamp = row[2]  # 3rd column is the timestamp
            if raw_timestamp:
                try:
                    return datetime.fromtimestamp(float(raw_timestamp.split('.')[0]))
                except ValueError:
                    return None
            return None

        parse_task = progress.add_task("[cyan]Parsing timestamps...", total=None)
        data = etl.addfield(data, "parsed_time", parse_timestamp)
        progress.update(parse_task, completed=True)

        # Filter rows with valid timestamps and AS path information
        typer.echo("Filtering update messages with valid AS paths...")
        as_path_col = 11  # 12th column contains the AS path
        filter_task = progress.add_task("[cyan]Filtering rows...", total=None)
        data = etl.select(data, lambda row: row["parsed_time"] is not None and row[as_path_col])
        progress.update(filter_task, completed=True)

        # Add AS path length column
        typer.echo("Calculating AS path lengths...")
        def as_path_length(row):
            as_path = row[as_path_col]
            return len(as_path.split()) if as_path else 0

        as_path_task = progress.add_task("[cyan]Adding AS path lengths...", total=None)
        data = etl.addfield(data, "as_path_length", as_path_length)
        progress.update(as_path_task, completed=True)

        # Sort the data by parsed timestamp
        typer.echo("Sorting data by parsed timestamp...")
        sort_task = progress.add_task("[cyan]Sorting rows...", total=None)
        data = etl.sort(data, "parsed_time")
        progress.update(sort_task, completed=True)

        # Process rows to calculate feature_3
        typer.echo("Processing rows to calculate feature_3...")
        current_window = []
        result = []

        process_task = progress.add_task("[cyan]Processing time windows...", total=None)
        for row in data.dicts():
            if row['parsed_time'] >= start_time + timedelta(seconds=window):
                # Compute the average AS path length for the completed window
                if current_window:
                    avg_length = sum(r['as_path_length'] for r in current_window) / len(current_window)
                else:
                    avg_length = 0
                result.append({"feature_name": "avg_as_path_length", "timestamp": start_time, "value": avg_length})

                # Advance the window
                start_time += timedelta(seconds=window)
                current_window = []

            # Add the current row to the window
            current_window.append(row)
        progress.update(process_task, completed=True)

        # Append the remaining data for the last time window
        if current_window:
            avg_length = sum(r['as_path_length'] for r in current_window) / len(current_window)
            result.append({"feature_name": "avg_as_path_length", "timestamp": start_time, "value": avg_length})

        # Write the results to the output file
        typer.echo(f"Writing results to output file: {output}")
        result_table = etl.fromdicts(result)
        write_output(output, result_table)
        typer.echo("Feature extraction complete!")


if __name__ == "__main__":
    app()
