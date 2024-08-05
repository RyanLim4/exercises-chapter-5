"""Implements reverse Polnish calculator."""
from numbers import Number
from math import sin, cos


class RPCalc:
    """A reverse Polnish Calculator."""

    def __init__(self):
        """Create the calculator."""
        self.stack = []

    def push(self, n):
        """Get the next input."""
        if isinstance(n, Number):
            self.stack.append(n)
        elif n == "sin":
            operand = self.pop()
            self.push(sin(operand))
        elif n == "cos":
            operand = self.pop()
            self.push(cos(operand))
        elif n == "+":
            operand2 = self.pop()
            operand1 = self.pop()
            self.push(operand1 + operand2)
        elif n == "-":
            operand2 = self.pop()
            operand1 = self.pop()
            self.push(operand1 - operand2)
        elif n == "*":
            operand2 = self.pop()
            operand1 = self.pop()
            self.push(operand1 * operand2)
        elif n == "/":
            operand2 = self.pop()
            operand1 = self.pop()
            self.push(operand1 / operand2)
        else:
            return

    def pop(self):
        """Pop item on internal stack and returns it."""
        if len(self):
            return self.stack.pop()
        else:
            return

    def peek(self):
        """Display top item on internal stack."""
        if len(self):
            return self.stack[-1]
        else:
            return

    def __len__(self):
        """Return length of internal stack."""
        return len(self.stack)
