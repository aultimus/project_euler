# https://projecteuler.net/problem=43

import doctest
import itertools


def gen_pandigital_strings(digits):
    """
    >>> gen_pandigital_strings("123")
    ['123', '132', '213', '231', '312', '321']
    """
    return ["".join(p) for p in itertools.permutations(digits)]


def has_substring_divisibility(d):
    """
    >>> has_substring_divisibility("1406357289")
    True
    """
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all(not(int(d[i + 1: i + 4]) % divisors[i]) for i in xrange(0, 7))

doctest.testmod()

pandigitals = [p for p in gen_pandigital_strings("0123456789") if p[0] != "0"]
print sum([int(p) for p in pandigitals if has_substring_divisibility(p)])
