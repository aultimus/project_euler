# http://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that # all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz(n):
    """ Returns number of values in collatz sequence starting at arg n"""
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 0:  # even
            n = n / 2
        else:
            n = 3 * n + 1
    return count

def main():
    m = 0  # max collatz chain size so far
    n = 0  # start of max collatz chain so far
    for i in xrange(1, 1000001):
        t = collatz(i)
        if t > m:
            n, m = i, t
    return n

if __name__ == "__main__":
    print main()
