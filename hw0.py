
# If you like these, check out https://projecteuler.net/archives

def is_even(n):
    """
    Check if a number n is even.

    Functions can return a value, which means that when the caller uses it they get the value back.

    >>> is_even(2)
    True
    >>> is_even(4) != is_even(2)
    False

    """


def is_prime(n):
    """ A prime number has exactly two factors, itself and n.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(1)
    False
    >>> is_prime(9)
    False
    """


def count_primes(n):
    """
    Count the number of primes which are less than or equal to n
    >>> import utils
    >>> count_primes(5)
    3
    >>> print(utils.calculate_sha256(str(count_primes(104743))))
    e443169117a184f91186b401133b20be670c7c0896f9886075e5d9b81e9d076b

    For extra credit... solve this in O(n * log log n) email Rohan if interested.

    :param n:
    :return:


    """

def multiples_sum(n):
    """
    Find the sum of the numbers 1 through n which are multiples of 3 or 5
    >>> multiples_sum(10)
    23
    >>> import utils
    >>> print(utils.calculate_sha256(str(multiples_sum(1000))))
    c0b20f4665d0388d564f0b6ecf3edc9f9480cb15fff87198b95701d9f5fe1f7b
    
    :return: R
    """
    s = 0
    # Load up the s variable and prepare it to be returned

    return s