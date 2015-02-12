# https://projecteuler.net/problem=28
#
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

def sum_number_spiral(dim):
    """
    >>> sum_number_spiral(5)
    101
    """
    total = 0
    n = dim - 1       # Difference between numbers in spiral
    x = (dim) ** 2    # starting number in top right of the square
    while x != 1:
        for __ in xrange(0, 4):  # Four corners each round
            #print x, n
            total += x
            x = x - n
        n -= 2
    return total + 1

def main():
    return sum_number_spiral(1001)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
