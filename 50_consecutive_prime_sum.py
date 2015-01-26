# https://projecteuler.net/problem=50

import doctest
import utils


def longest_consec_prime_sum_below_n(n):
    """
    >>> longest_consec_prime_sum_below_n(100)
    41
    >>> longest_consec_prime_sum_below_n(1000)
    953
    """
    primes = [p for p in utils.sieveOfEratosthenes(n)]
    hashed_primes = set(primes)  # faster but what about mem constraints
    max_prime_run = []
    for i in xrange(0, len(primes)):
        for j in xrange(i + 1, len(primes) + 1):
            prime_run = primes[i:j]
            s = sum(prime_run)
            if s >= n:
                break
            elif len(prime_run) > len(max_prime_run) and s in hashed_primes:
                # print prime_run, s
                max_prime_run = prime_run
    return sum(max_prime_run)

doctest.testmod()

print longest_consec_prime_sum_below_n(1000000)
