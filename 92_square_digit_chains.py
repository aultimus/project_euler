import array


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
    result = 0
    while n:
        result += (n % 10) * (n % 10)
        n /= 10
    return result


def is_eighty_niner(n):
    while n > 1:
        if n == 89:
            return True
        n = square_sum_of_digits(n)
    return False


def main():
    # This is the highest possible value in the chain
    assert(square_sum_of_digits(9999999) == 567)
    eighty_niners = array.array('B', [is_eighty_niner(i) for i in xrange(567 + 1)])

    count = 0
    for i in xrange(2, 10000000):
        if eighty_niners[square_sum_of_digits(i)]:
            count += 1

    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import time
    start = time.time()
    print main()
    print "seconds taken:", time.time() - start
