# http://projecteuler.net/problem=20
# n! means n x (n - 1) x ... x 3 x 2 x 1
#
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800 and
# the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import math

def main():
    x = math.factorial(100)
    l = list(str(x))

    return sum([int(i) for i in l])

if __name__ == "__main__":
    print main()
