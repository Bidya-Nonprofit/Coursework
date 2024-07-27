"""
Classwork 1 on functions and function composition.
"""

from typing import Callable, Tuple

# Closed function from integers to integers.
UnaryInt = Callable[[int], int]

def fib(n):
    if n <= ...:
        return n
    else:
        return fib(...) + fib(...)

def sum_f(f: UnaryInt, count: int) -> int:
    """
    Return f(0) + f(1) + ... f(count - 1)
    :param fib:
    :param count:
    :return:
    >>> sum_fibonacci_numbers(fib, 8) = sum([0, 1, 1, 2, 3, 5, 8, 13])
    """

    running_sum = 0

    for i in range(...):
        running_sum += f(...)

    return ...


def get_linear_function(m: int, b: int = 0) -> UnaryInt:
    """
    Return the affine function mx + b. If B is not specified, it defaults to 0

    >>> all(x == get_linear_function(1)(x) for x in range(24))
    True
    >>> all(((10 * x + 5) == get_linear_function(10, 5)(x)) for x in range(24))
    True

    :return:
    """

    def inner(x):
        return ... + ...

    return inner

def compose(f: UnaryInt, g: UnaryInt) -> UnaryInt:
    """
    Given functions f and g, return f(g(x))
    :param f:
    :param g:
    :return: f(g(x))
    >>> x6 = compose(lambda x : 2 * x, lambda x: 3 * x)
    >>> all(x6(x) == get_linear_function(6, 0)(x) for x in range(24))
    True
    """

    return lambda x: f(g(x))


def iterate(f: UnaryInt, count: int) -> UnaryInt:
    """
    Return a new function f(x) count number of times to x.

    :param f:
    :param count:
    :return:

    >>> double = lambda x : 2 * x
    >>> [iterate(double, i)(x) for x in range(7)]
    [1, 2, 4, 8, 16, 32, 64]
    """

    if count == 0:
        return lambda x : ...
    else:
        g = iterate(f, count - 1)
        return compose(..., ...)


def minimize(f: UnaryInt, lb: int, ub: int) -> Tuple[int, int]:
    """
    Find the value of x, and f(x) such that f(x) is minimized and x is between lb and ub where x is an integer.
    :param f:
    :param lb: The lower bound of the search range inclusive
    :param ub: The upper bound of the search range exclusive
    :return: (x, f(x))
    >>> minimize(lambda x: x, 0, 10)
    (0, 0)
    >>> minimize(lambda x: (x - 20) ** 2 + 100, -100, 100) # (x - 20)^2 + 100
    (20, 100)
    """
    best, fbest = lb - 1, float("-inf")

    for x in range(lb, ub):
        f_x = f(...)
        if ... < ...:
            best, fbest = ..., ...

    return best, fbest
