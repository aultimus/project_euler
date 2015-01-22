# https://projecteuler.net/problem=52
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

import doctest


def make_digits_list(x):
    """
    >>> make_digits_list(54321)
    ['1', '2', '3', '4', '5']
    """
    digits = list(str(x))
    digits.sort()
    return digits

doctest.testmod()


def has_permuted_multiples(x):
    digits = make_digits_list(x)
    for m in [2, 3, 4, 5, 6]:
        if make_digits_list(x * m) != digits:
            return False
    return True

for x in xrange(1, 10000000000):
    if has_permuted_multiples(x):
        print x
        break
