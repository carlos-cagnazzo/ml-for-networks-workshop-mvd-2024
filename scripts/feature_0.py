#!/usr/bin/env python3

import typer
import petl as etl
from datetime import datetime, timedelta
from common import read_input, write_output, progress_bar

app = typer.Typer()

@app.command()
def extract_feature_0(
    input: str = typer.Option(..., "--input", help="Input CSV file"),
    head: int = typer.Option(None, "--head", help="Number of rows to process"),
    output: str = typer.Option(..., "--output", help="Output CSV file"),
    window: int = typer.Option(300, "--window", help="Time window size in seconds")
):
    """
    Extract feature_0: Number of BGP update messages per time window.
    """
    # Load the data using PETL
    data = read_input(input, head)
    timestamp_col = 2  # Assuming timestamp is the 3rd column (0-indexed)

    # Function to parse and handle timestamps
    def parse_timestamp(row):
        raw_timestamp = row[timestamp_col]
        if raw_timestamp:  # Ensure the timestamp is not empty
            try:
                # Parse the timestamp, handling fractional seconds
                return datetime.fromtimestamp(float(raw_timestamp.split('.')[0]))
            except ValueError:
                typer.echo(f"Skipping invalid timestamp: {raw_timestamp}")
                return None
        return None

    # Add a parsed timestamp column
    data = etl.addfield(data, "parsed_time", parse_timestamp)
    
    # Print first few rows for debugging
    print("First rows after adding parsed_time:")
    print(etl.look(data, 5))

    # Filter rows with valid timestamps
    data = etl.select(data, lambda row: row["parsed_time"] is not None)
    
    # Print first few rows after filtering
    print("First rows after filtering invalid timestamps:")
    print(etl.look(data, 5))
    
    # Sort the data by parsed timestamp
    data = etl.sort(data, "parsed_time")
    
    # Print first few rows after sorting
    print("First rows after sorting:")
    print(etl.look(data, 5))

    start_time = None
    current_window = []
    result = []

    # Process rows with a progress bar
    for row in progress_bar(data.dicts(), description="Processing BGP updates"):
        if start_time is None:
            start_time = row['parsed_time']

        # Check if the current row is outside the time window
        if row['parsed_time'] >= start_time + timedelta(seconds=window):
            # Store the count for the completed time window
            result.append({"feature_0": "update_count", "timestamp": start_time, "value": len(current_window)})
            # Advance the window
            start_time = row['parsed_time']
            current_window = []

        # Add the current row to the window
        current_window.append(row)

    # Append the remaining data for the last time window
    if current_window:
        result.append({"feature_0": "update_count", "timestamp": start_time, "value": len(current_window)})

    # Debugging: Print the result list before writing to output
    print("Generated results:")
    for res in result[:5]:  # Print first 5 results for debugging
        print(res)

    # Write the results to the output file
    result_table = etl.fromdicts(result)
    write_output(output, result_table)


if __name__ == "__main__":
    app()

