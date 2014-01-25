# http://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# sum of squares
n = 0
for i in xrange(0,101):
    n += i ** 2

# square of sum
m = 0
for i in xrange(1,101):
    m += i
m = m ** 2

print m - n
