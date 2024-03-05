#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Default is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

# Test cases
print(add_integer(1, 2))      # Output: 3
print(add_integer(100, -2))   # Output: 98
print(add_integer(2))         # Output: 100
print(add_integer(100.3, -2)) # Output: 98

# Exception cases
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)  # Output: b must be an integer

try:
    print(add_integer(None))
except Exception as e:
    print(e)  # Output: a must be an integer

