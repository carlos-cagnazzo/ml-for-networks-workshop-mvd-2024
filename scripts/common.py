#!/usr/bin/env python3

import typer
from rich.progress import Progress
import petl as etl

def read_input(input_file: str, head: int = None):
    """
    Reads the input BGP data file with PETL.
    """
    data = etl.fromcsv(input_file)
    if head:
        data = etl.head(data, head)
    return data

def write_output(output_file: str, table):
    """
    Writes the output table to a CSV file.
    """
    etl.tocsv(table, output_file)

def progress_bar(iterable, description="Processing"):
    """
    Wraps an iterable with a Rich progress bar.
    """
    with Progress() as progress:
        task = progress.add_task(description, total=len(iterable))
        for item in iterable:
            yield item
            progress.update(task, advance=1)

