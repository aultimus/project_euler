# http://projecteuler.net/problem=48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
import sys
#for i in xrange()

print str(sum([i**i for i in xrange(1,1000)]))[-10:]
