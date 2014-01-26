# http://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Not enough RAM to run sieve of erastosthenes for such a large num
from utils import trialDivision

num = 600851475143

for prime in trialDivision(num):
    print prime
