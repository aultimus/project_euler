def digit_sum(n):
    """
    >>> digit_sum(100**100)
    1
    >>> digit_sum(2**50)
    76
    """
    return sum(int(x) for x in list(str(n)))


def main():
        return max([digit_sum(a ** b) for a in xrange(1, 100)
                    for b in xrange(1, 100)])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
