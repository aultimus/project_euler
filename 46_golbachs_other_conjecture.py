# https://projecteuler.net/problem=46

import utils


prime_ceil = 100000
square_ceil = 1000

primes = set([p for p in utils.sieveOfEratosthenes(prime_ceil)])
odd_composite_nums = [c for c in xrange(0, prime_ceil)
                      if c not in primes and c % 2 and c > 1]
assert(odd_composite_nums[:6] == [9, 15, 21, 25, 27, 33])  # data from question

# l is a list of all possible combinations of sum of a prime and twice a square
l = set([p + (2 * (s ** 2)) for p in primes for s in xrange(1, square_ceil)])

try:
    print [x for x in odd_composite_nums if x not in l][0]
except IndexError:
    print "No solution found within given range"
