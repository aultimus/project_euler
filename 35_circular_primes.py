# http://projecteuler.net/problem=35
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and # 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import utils

def main():
    primes = set([p for p in utils.sieveOfEratosthenes(1000000)])
    return len([p for p in primes if utils.get_rotations(p).issubset(primes)])


if __name__ == "__main__":
    print main()
