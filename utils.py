from array import array

# Sieve of Eratosthenes
def sieveOfEratosthenes(c):
    """
    Generates prime numbers using sieve of Eratosthenes algorithm
    1. Create a list of consecutive integers from 2 through
        n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the first prime number.
    3. Starting from p, enumerate its multiples by counting to n in increments
        of p, and mark them in the list (these will be 2p, 3p, 4p, etc.;
        the p itself should not be marked).
    4. Find the first number greater than p in the list that is not marked.
    5. If there was no such number, stop. Otherwise, let p now equal this new
        number (which is the next prime), and repeat from step 3.

    arg c: upper limit on prime numbers you want to generate

    >>> r = [p for p in sieveOfEratosthenes(114)]
    >>> r == [2, 3, 5,7, 11, 13, 17, 19, 23, 29,
    ... 31, 37, 41, 43, 47,  53,  59,  61,  67,  71,
    ... 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    True
    """
    def mark(x):
        for i in xrange(x*2,len(n),x):
            n[i] = 0
    n = array('B', [1 for i in xrange(c)])
    p = 0
    marked = False
    for i in xrange(2, c):
      if n[i] and i > p:
            p = i
            yield p
            mark(p)

def isPrime(n, cache=[]):
    """ brute force prime checker """
    if n in cache:
        return True
    for i in xrange(2, n):
        if n % i == 0:
            return False
    cache.append(n)
    return True

def trialDivision(n):
    """ brute force prime factor finder """
    for i in xrange(2, n):
        if n % i == 0 and isPrime(i):
            yield i

def gcd(x, y):
    """
    Greatest Common Divisor func, implementation of Euclid's algorithm

    >>> gcd(48,18)
    6
    >>> gcd(13, 35)
    1
    >>> gcd(27, 90)
    9
    """
    x, y = max(x,y), min(x,y)
    while y:
        x,y = y, x % y
    return x

def pollardsRho(n):
    f = lambda x: (x**2 -1) % n
    x = random.randint(1, n-1)
    y = random.randint(1, n-1)
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
    return d

def factorise(n):
    """ Return list of all factors of n
    >>> factorise(1)
    set([1])
    >>> factorise(21)
    set([1, 3, 21, 7])
    >>> factorise(28)
    set([1, 2, 4, 7, 14, 28])
    """
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def proper_divisors(n):
    """
    >>> proper_divisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> proper_divisors(284)
    [1, 2, 4, 71, 142]
    """
    return [i for i in xrange(1, (n/2)+1) if not n % i]

def sum_of_proper_divisors(n):
    """
    >>> sum_of_proper_divisors(220)
    284
    >>> sum_of_proper_divisors(284)
    220
    """
    return sum(proper_divisors(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
