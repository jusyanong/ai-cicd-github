"""Simple utility functions - you'll add more!"""


def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

def factorial(n):
    """Compute the factorial of a non-negative integer using recursion."""
    if n < 0:
        raise ValueError("factorial() is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
