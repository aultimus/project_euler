# https://projecteuler.net/problem=27

import doctest
import utils

prime_ceil = 10000000
primes = set([p for p in utils.sieveOfEratosthenes(prime_ceil)])


def q(n, a, b):
    return (n ** 2) + (a * n) + b  # better safe than sorry with precedence


def num_consecutive_primes(n, a, b, primes):
    """
    >>> num_consecutive_primes(0, -79, 1601, primes)
    80
    """
    while True:     # A do, while loop would be nice
        ans = q(n, a, b)
        assert(ans < prime_ceil)
        if ans in primes:
            n += 1
        else:
            break
    return n


def product_of_coefficients(a, b):
    """
    >>> product_of_coefficients(-79, 1601)
    -126479
    """
    return a * b

doctest.testmod()


a_b_ceil = 1000
longest_consec_primes = 0, 0, 0

for a in xrange(-a_b_ceil, a_b_ceil):
    for b in xrange(-a_b_ceil, a_b_ceil):
        num_primes = num_consecutive_primes(0, a, b, primes)
        if num_primes > longest_consec_primes[2]:
            longest_consec_primes = a, b, num_primes

print product_of_coefficients(longest_consec_primes[0],
                              longest_consec_primes[1])
