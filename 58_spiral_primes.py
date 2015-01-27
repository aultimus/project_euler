import doctest
import utils

max_dim = 50000

def prime_percentage(dim, num_primes):
    """
    >>> prime_percentage(7, 8)
    61.53846153846154
    """
    num_diagonals = (dim * 2) - 1  # num of nums in spiral lying on diagonals
    return (num_primes / float(num_diagonals)) * 100

def spiral_num_diag_primes(dim, num_primes_in_prev):
    """
    >>> spiral_num_diag_primes(7, 5, primes)
    8
    """
    num_primes = 0
    n = dim - 1       # difference between numbers in spiral
    x = dim ** 2      # (dim * dim) is max num in number spiral
    for __ in xrange(4):  # Four corners
    # Not enough memory to use sieve
        if utils.is_prime_cacheless(x):
            num_primes += 1
        x = x - n
    return num_primes + num_primes_in_prev


doctest.testmod()


num_primes = 5      # when dim = 5
for dim in xrange(7, max_dim, 2):
    num_primes = spiral_num_diag_primes(dim, num_primes)
    percentage = prime_percentage(dim, num_primes)
    if percentage < 10:
        print "result", dim, percentage
        break
    elif not dim % 7:
        print dim, percentage