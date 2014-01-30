
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
    n = [1 for i in xrange(c)]
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
