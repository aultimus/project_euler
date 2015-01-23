# https://projecteuler.net/problem=53
# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
# nCr = n! / r!(n-r)!
# where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
#


# nCr when 1<= n <= 100
# strictly: r <= n

import utils


print len([n for n in xrange(1,101) for r in xrange(1,n)
            if utils.binomial_coefficient(n,r) > 1000000])