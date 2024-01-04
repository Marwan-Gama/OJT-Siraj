"""
• Python follows the convention of many computer languages in choosing to define 00= 1
• Write a function, power(a, b), which behaves the same as the Python expression a**b, but raises a ValueError
if a and b are both zero
• Also, if a or b are not numbers, the function should raise a TypeError
• Write a proper docstring for the function including the description of the raised exception
"""


def power(a, b):
    """
    Computes the exponentiation of 'a' raised to the power of 'b'.

    Args:
    a (int, float): Base number.
    b (int, float): Exponent.

    Returns:
    float or int: Result of 'a' raised to the power of 'b'.

    Raises:
    TypeError: If either 'a' or 'b' is not a number (int or float).
    ValueError: If both 'a' and 'b' are zero (0 ** 0 is undefined).
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both 'a' and 'b' must be numbers (int or float)")

    if a == b == 0:
        raise ValueError("Both 'a' and 'b' cannot be zero (0 ** 0 is undefined)")

    return a ** b
