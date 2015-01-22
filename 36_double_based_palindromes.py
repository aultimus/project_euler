# https://projecteuler.net/problem=36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

import doctest
import utils


def is_palindrome_in_binary(x):
    """
    >>> is_palindrome_in_binary(585)
    True
    """
    b = "{0:b}".format(x)
    # extra work in int conversion but is necessary to use utility function
    return utils.is_palindrome(int(b))


def is_palindrome_in_decimal(x):
    """
    >>> is_palindrome_in_decimal(585)
    True
    """
    return utils.is_palindrome(x)


def is_palindrome_in_dec_and_bin(x):
    """
    >>> is_palindrome_in_dec_and_bin(585)
    True
    """
    return is_palindrome_in_decimal(x) and is_palindrome_in_binary(x)

doctest.testmod()

print sum([i for i in xrange(1, 1000000) if is_palindrome_in_dec_and_bin(i)])
