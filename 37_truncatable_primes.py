# http://projecteuler.net/problem=37
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
# left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left
# to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from utils import sieveOfEratosthenes


def getTruncations(n):
    """
    >>> r = getTruncations(3797)
    >>> r == {797, 97, 7, 379, 37, 3}
    True
    """
    s = str(n)
    ln = len(s)
    r = set()
    for i in xrange(1, len(s)):
        r.add(int(s[:-i]))
        r.add(int(s[-i:]))
    return r

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    total = 0
    primes = [p for p in sieveOfEratosthenes(1000000)]
    for p in primes:
        if p > 9 and all(t in primes for t in getTruncations(p)):
            total += p
    print total
