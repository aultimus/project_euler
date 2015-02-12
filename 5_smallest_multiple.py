# http://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

# 1 -> 10 are factors of 10 -> 20
for i in xrange(20, 1000000000):
    for j in xrange(10, 21):
        if i % j:
            break
        if j == 20:
            print i
