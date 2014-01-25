# http://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10 001st prime number?

#   Sieve of Eratosthenes
#   1. Create a list of consecutive integers from 2 through
#   n: (2, 3, 4, ..., n).
#   2. Initially, let p equal 2, the first prime number.
#   3. Starting from p, enumerate its multiples by counting to n in increments
#   of p, and mark them in the list (these will be 2p, 3p, 4p, etc.;
#   the p itself should not be marked).
#   4. Find the first number greater than p in the list that is not marked.
#   5. If there was no such number, stop. Otherwise, let p now equal this new
#   number (which is the next prime), and repeat from step 3.

# Add actual integer vals for readability rather than using indexes
# [number, marked]

from utils import genPrimes

count = 0
for prime in genPrimes(1000000):
    count += 1
    if count == 10001:
        print prime
