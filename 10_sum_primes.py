# http://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from utils import sieveOfEratosthenes

n = 0
for prime in sieveOfEratosthenes(2000000):
    n += prime
print n
