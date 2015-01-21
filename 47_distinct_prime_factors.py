# http://projecteuler.net/problem=47

import doctest, time, utils

def get_prime_factors_list(x, primes):
    """ Return list of prime factors of x given list of primes
    >>> primes = [p for p in utils.sieveOfEratosthenes(1000)]
    >>> get_prime_factors_list(14, primes)
    [2, 7]
    >>> get_prime_factors_list(15, primes)
    [3, 5]
    >>> get_prime_factors_list(644, primes)
    [2, 7, 23]
    >>> get_prime_factors_list(645, primes)
    [3, 5, 43]
    >>> get_prime_factors_list(646, primes)
    [2, 17, 19]
    """
    f_list = utils.factorise(x)
    return [f for f in f_list if f in primes]

doctest.testmod()
start = time.time()

limit = 200000
num_prime_facs = 4
primes = [p for p in utils.sieveOfEratosthenes(limit)]
count = 0

for i in xrange(1, limit):
    if not i % 1000:
        print i
    p_facs = get_prime_factors_list(i, primes)
    if len(p_facs) >= num_prime_facs:
        count+=1
    else:
        count = 0

    if count == num_prime_facs:
        print "result: %d" % (i - (num_prime_facs-1))
        break
print "wall-clock time taken: %d" % (time.time() - start)
