# http://projecteuler.net/problem=35
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and # 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import utils


def get_rotations(n):
    """
    >>> r = get_rotations(197)
    >>> r == {971, 719}
    True
    >>> r = get_rotations(15)
    >>> r == {51}
    True
    """
    rots = set()
    if n >= 10:
        digits = str(n)
        for i in xrange(1, len(digits)):
            digits = digits[-1:] + digits[:-1]
            rots.add(int(digits[:]))
    return rots

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    count = 0
    primes = set([p for p in utils.sieveOfEratosthenes(1000000)])
    for p in primes:
        if all(r in primes for r in get_rotations(p)):
            count += 1
    print count
