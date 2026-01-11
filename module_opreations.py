def addition(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtraction(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiplication(a, b):
    """Returns the product of a and b."""
    return a * b

def division(a, b):
    """Returns the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def square_root(a):
    """Returns the square root of a. Raises ValueError if a is negative."""
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return a ** 0.5

def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b
def exponents(a, b):
    """Returns a raised to the power of b."""
    return a ** b

def random2(a, b):
    """Returns a random integer between a and b (inclusive)."""
    import random2
    return random2.randint(a, b)
    