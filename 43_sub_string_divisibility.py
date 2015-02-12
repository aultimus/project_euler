# https://projecteuler.net/problem=43

import itertools
import utils


def has_substring_divisibility(d):
    """
    >>> has_substring_divisibility("1406357289")
    True
    """
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all(not(int(d[i + 1: i + 4]) % divisors[i]) for i in xrange(0, 7))


def main():
    pandigitals = [p for p in utils.gen_pandigital_strings("0123456789")
                   if p[0] != "0"]
    return sum([int(p) for p in pandigitals if has_substring_divisibility(p)])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
