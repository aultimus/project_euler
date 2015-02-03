import doctest
import time

def square_sum_of_digits(n):
    """
    >>> square_sum_of_digits(44)
    32
    >>> square_sum_of_digits(32)
    13
    >>> square_sum_of_digits(13)
    10
    >>> square_sum_of_digits(4)
    16
    >>> square_sum_of_digits(1)
    1
    """
    return sum([int(d) ** 2 for d in str(n)])

doctest.testmod()

start = time.time()
eighty_niners = set()
for i in xrange(2, 10000000):
    if not i % 100000:
        print i
    n = i
    chain = []
    while n != 1:
        chain.append(n)
        if n in eighty_niners or n == 89:
            eighty_niners.update(chain)
            break
        n = square_sum_of_digits(n)

print len([x for x in eighty_niners if x < 10000000])
print "seconds taken:", time.time() - start
