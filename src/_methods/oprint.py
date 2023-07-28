import sys

from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table
from rich import box
from rich.console import Console
from dataclasses import fields


console = Console()


# print orbit in a pretty way
def oprint(obj):
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("Field")
    table.add_column("Value")

    try:
        for field in fields(obj):
            value = getattr(obj, field.name)
            if value is not None:
                table.add_row(field.name, str(value))
    except TypeError as e:
        console.print_exception(show_locals=True)
        sys.exit()

    console.print(table)
