from rich.console import Console
from rich import box

class TooManyInputs(Exception):
    def __init__(self, message, **kwargs):
        super().__init__(message)
        self.values = kwargs

    def __str__(self):
        if self.values:
            return f"\033[91m{type(self).__name__}: {self.values=}\033[0m"
        else:
            return f"\033[91m{type(self).__name__}\033[0m"
