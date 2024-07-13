import utils

def square(n):
    """Print a square to the console using asterisks. Which is nxn...

    free bee.
    >>> square(5)
    *****
    *****
    *****
    *****
    *****

    :param n:
    :return:
    """

    # for each line
    for i in range(n):
        # print the line
        for j in range(n):
            print("*", end = "")
        print("\n", end ="")

def pyramid(n):
    """ Print a pyramid of asterisks with n levels.

    The first line has Each line should have one more asterisk then the previous line.
    >>> pyramid(1)
    *
    >>> pyramid(4)
    *
    **
    ***
    ****

    :param n: Number of lines in the pyramid
    :return: None
    """
    for i in range(n):
        for j in range(i + 1):
            print("*", end = "")
        print("")



def fizz_buzz(n):
    """
    Takes in a number n... Then prints to console the numbers 1... n on separate lines with a twist...
    For each number, if it is divisible by 3, print "Fizz" if it is divisible by 5 print "Buzz" and if it is divisible
    by both print("FizzBuzz")
    >>> fizz_buzz(1)
    1
    >>> fizz_buzz(5)
    1
    2
    Fizz
    4
    Buzz
    >>> # Capture print statements... this is hacky and bad.
    >>> arr = []
    >>> old_print = print
    >>> import class0
    >>> class0.print = (lambda st: arr.append(str(st)))
    >>> fizz_buzz(49)
    >>> st = "\\n".join(arr)
    >>> # https://en.wikipedia.org/wiki/Cryptographic_hash_function
    >>> utils.calculate_sha256(st) # This allows us to check your output without us sharing the answer with you
    'ae5aff81cc3bc620a947e684b9e7c3e11abe9dc0dc4f310b2d73b70f4f061e49'
    >>> class0.print = old_print

    :param n: Number of FizzBuzz entries
    :return: None
    """
    for i in range(1, n + 1): # Range operations start at the start bound and go up to the end exclusive
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)



