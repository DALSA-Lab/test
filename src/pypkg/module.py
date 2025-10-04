"""
module.py - A dummy module for demonstration

This module contains simple functions with docstrings for MkDocs API documentation.
"""

def add(a, b):
    """
    Add two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def greet(name):
    """
    Generate a greeting message.

    Args:
        name (str): Name of the person.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"