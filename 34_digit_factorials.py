# http://projecteuler.net/problem=34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import math

def main():
    l = []
    for i in xrange(30, 1000000):
        digits = list(str(i))
        s = sum(math.factorial(int(d)) for d in digits)
        if i == s:
            l.append(i)
    return sum(l)

if __name__ == "__main__":
    print main()
