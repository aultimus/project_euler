# http://projecteuler.net/problem=21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import doctest
import utils

def proper_divisors(n):
    """
    >>> proper_divisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> proper_divisors(284)
    [1, 2, 4, 71, 142]
    """
    return [i for i in xrange(1, (n/2)+1) if not n % i]

def sum_of_proper_divisors(n):
    """
    >>> sum_of_proper_divisors(220)
    284
    >>> sum_of_proper_divisors(284)
    220
    """
    return sum(proper_divisors(n))

def are_amicable(a, b):
    """
    >>> are_amicable(220, 284)
    True
    """
    if a == b:
        return False
    return (sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a)

doctest.testmod()

l = set()
amicable_total = 0
for a in xrange(1, 10001):
    if not a % 500:
        print a
    b = sum_of_proper_divisors(a) # doing this calc twice, could cache or pass in
    if are_amicable(a,b):
        l.add(a)
        l.add(b)
print l
print "result", sum(l)

