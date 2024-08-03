"""
Classwork 1 on functions and function composition.

Takeaways from class 1.

Expressions represent the composition of functions and evaluate to a single value.
- Primitive expressions (think, ints, bools etc...)
- Compound expressions
How are functions evaluated in infix notation.

First evaluate function, then evaluate the arguments. Then apply the function to the arguments.

Integers are Immutable...

A higher order function is a function that takes one or more functions as
arguments or returns a function as a result.

"""

from typing import Callable, Tuple

# Closed function from integers to integers.
UnaryInt = Callable[[int], int]


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def sum_f(f, count) -> int:
    """
    Return f(0) + f(1) + ... f(count - 1)
    :param fib:
    :param count:
    :return:
    >>> assert sum_f(fib, 8) == sum([0, 1, 1, 2, 3, 5, 8, 13])
    """

    running_sum = 0

    for i in range(count):  # inside of this loop. `i` will range from 0... n -1
        running_sum += f(i)

    return running_sum


assert sum_f(fib, 8) == sum([0, 1, 1, 2, 3, 5, 8, 13])


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
        return m * x + b

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
    >>> [iterate(double, i)(1) for i in range(7)]
    [1, 2, 4, 8, 16, 32, 64]
    """

    if count == 0:
        return lambda x: x
    else:
        g = iterate(f, count - 1)
        return compose(f, g)


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
    old_best_x, old_best_f_x = lb - 1, float("inf")

    for new_x in range(lb, ub):
        new_best = f(new_x)
        if new_best < old_best_f_x:  # if we have a new best that is less than the old best
            old_best_x, old_best_f_x = new_x, new_best  # update our old best with this new value of x and f(x)

    return old_best_x, old_best_f_x