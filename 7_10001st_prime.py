# http://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10 001st prime number?

from utils import sieveOfEratosthenes

count = 0
for prime in sieveOfEratosthenes(1000000):
    count += 1
    if count == 10001:
        print prime
