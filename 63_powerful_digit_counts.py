# https://projecteuler.net/problem=63

def gen_n_powers(n):
    """
    Generate all n-digit positve integers that are also a power of n
    >>> 16807 in gen_n_powers(5)
    True
    >>> 134217728 in gen_n_powers(9)
    True
    """
    l = []
    i = 1
    while True:
        p = i ** n
        len_n = len(str(p))
        if len_n == n:
            l.append(p)
        elif len_n > n:
            return l
        i += 1

def main():
    count = 0
    for i in xrange(1, 1001):
        count += len(gen_n_powers(i))
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
