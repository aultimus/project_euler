# https://projecteuler.net/problem=15
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Take the 2x2 grid, we can only move down twice and right twice.
# So we have four moves, each either being right or down.
# There are six possible paths, this can be represented as a four bit string
# with two bits being 1 (right) and two being down (0).
# 1100
# 1010
# 1001
# 0110
# 0101
# 0011
# so the question is how many permutations are there of a string of len 2n which
# has n 0s and n 1s. Online research points to the binomial coefficient.

# http://en.wikipedia.org/wiki/Binomial_coefficient#Binomial_coefficient_in_programming_languages
from math import factorial
def binomialCoefficient(n, k):
    """
    from n positions choose k
    >>> binomialCoefficient(4,2)
    6
    """
    return factorial(n) // (factorial(k) * factorial(n - k))

print binomialCoefficient(40,20)
