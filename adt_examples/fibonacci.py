"""Class fib implements the fibonacci sequence."""


class Fib:
    """Fibonacci class."""

    def __init__(self):
        """Construct Fib starting at 0 and 1."""
        self.cur = 0
        self.next = 1

    def __iter__(self):
        """Implement iterator protocol."""
        return self

    def __next__(self):
        """Iterate step."""
        self.cur, self.next = self.next, self.cur + self.next
        return self.next
