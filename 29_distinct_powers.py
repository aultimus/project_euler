# https://projecteuler.net/problem=29
import doctest


# Cannot for the life of me think of a good name for this function
def a_to_b_range(a_min, a_max, b_min, b_max):
    """
    >>> l = a_to_b_range(2, 5, 2, 5)
    >>> l
    [4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125]
    >>> len(l)
    15
    """
    vals = list(set([a ** b for a in xrange(a_min, a_max + 1)
                            for b in xrange(b_min, b_max + 1)]))
    vals.sort()
    return vals


doctest.testmod()

print len(a_to_b_range(2, 100, 2, 100))
