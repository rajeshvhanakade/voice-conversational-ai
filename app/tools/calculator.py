# app/tools/calculator.py

import re

def run(text: str):
    """
    Extracts a math expression from text and evaluates it.
    Example: '2 plus 2' -> 4
    """

    expr = text.lower()

    # word replacements
    expr = expr.replace("plus", "+")
    expr = expr.replace("minus", "-")
    expr = expr.replace("times", "*")
    expr = expr.replace("multiplied by", "*")
    expr = expr.replace("divide", "/")
    expr = expr.replace("divided by", "/")

    # keep only numbers and operators
    expr = re.sub(r"[^0-9+\-*/().]", "", expr)

    if not expr:
        raise ValueError("No math expression found")

    return eval(expr)