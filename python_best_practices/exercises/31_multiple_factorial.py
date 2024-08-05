import math
from concurrent.futures import ThreadPoolExecutor

def factorial(x):
    # Assume this function performs a heavy computation
    return math.factorial(x)


def multiple_factorial(iterable):
    """
    For every element in `iterable`, prints the factorial of this element on a separate line.
    Performs well.
    >>> multiple_factorial(range(10))
    1
    1
    2
    6
    24
    120
    720
    5040
    40320
    362880
    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        for result in executor.map(factorial, iterable):
            print(result)