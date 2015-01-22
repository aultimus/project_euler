# http://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Cheaper than modulus? Probably, that would be 2000 moduluses!
l = [i for i in xrange(0, 1000, 3)]
l.extend([i for i in xrange(0, 1000, 5)])
s = set(l)
print sum(s)
