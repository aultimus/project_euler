import array
import itertools
import math
import operator

primes_to_114 = [2, 3, 5,7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,  53,
                59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

# Note: Generates primes upto but not including c
# Generator version - yields prime ints
def sieveOfEratosthenes(c):
    """
    Generates prime numbers using sieve of Eratosthenes algorithm
    1. Create a list of consecutive integers from 2 through
        n-1: (2, 3, 4, ..., n-1).
    2. Initially, let p equal 2, the first prime number.
    3. Starting from p, enumerate its multiples by counting to n in increments
        of p, and mark them in the list (these will be 2p, 3p, 4p, etc.;
        the p itself should not be marked).
    4. Find the first number greater than p in the list that is not marked.
    5. If there was no such number, stop. Otherwise, let p now equal this new
        number (which is the next prime), and repeat from step 3.

    arg c: upper limit on prime numbers you want to generate

    >>> [p for p in sieveOfEratosthenes(114)] == primes_to_114
    True
    >>> [p for p in sieveOfEratosthenes(11)]
    [2, 3, 5, 7]
    """
    def mark(x):
        for i in xrange(x * 2, len(n), x):
            n[i] = 0
    n = array.array('B', [1 for i in xrange(c)])
    p = 0
    marked = False
    for i in xrange(2, c):
        if n[i] and i > p:
            p = i
            yield p
            mark(p)

# More efficient yet less user friendly version, returns byte array
def sieve_byte_array(c):
    """
    >>> r = sieve_byte_array(114)
    >>> all(r[p] for p in primes_to_114)
    True
    """
    def mark(x):
        for i in xrange(x * 2, len(n), x):
            n[i] = 0
    n = array.array('B', [1 for i in xrange(c)])
    p = 0
    marked = False
    for i in xrange(2, c):
        if n[i] and i > p:
            p = i
            mark(p)
    return n


def isPrime(n, cache=set()):
    """ brute force prime checker """
    if n in cache:
        return True
    is_prime =  is_prime_cacheless(n)
    cache[n] = is_prime
    return is_prime



def is_prime_cacheless(n):
    """
    >>> primes = [is_prime_cacheless(p) for p in xrange(114)]
    >>> primes == [p in primes_to_114 for p in xrange(114)]
    True

    brute force prime checker
    """
    if n < 2:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
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
    x, y = max(x, y), min(x, y)
    while y:
        x, y = y, x % y
    return x


def pollardsRho(n):
    f = lambda x: (x ** 2 - 1) % n
    x = random.randint(1, n - 1)
    y = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
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
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def proper_divisors(n):
    """
    >>> proper_divisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> proper_divisors(284)
    [1, 2, 4, 71, 142]
    """
    return [i for i in xrange(1, (n / 2) + 1) if not n % i]


def sum_of_proper_divisors(n):
    """
    >>> sum_of_proper_divisors(220)
    284
    >>> sum_of_proper_divisors(284)
    220
    """
    return sum(proper_divisors(n))


def reverse_int(x):
    """
    >>> reverse_int(47)
    74
    """
    return int(str(x)[::-1])


def is_palindrome(x):
    """
    >>> is_palindrome(7337)
    True
    >>> is_palindrome(13441)
    False
    """
    return str(x) == str(x)[::-1]


def get_rotations(n):
    """
    Returns a set of integer permutations on int n.
    Doesn't currently handle negative numbers
    >>> get_rotations(197)
    set([971, 719])
    >>> get_rotations(15)
    set([51])
    >>> get_rotations(1234)
    set([4123, 3412, 2341])
    >>> get_rotations(10)
    set([1])
    """
    rots = set()
    if n >= 10:
        digits = str(n)
        for i in xrange(1, len(digits)):
            digits = digits[-1:] + digits[:-1]
            rots.add(int(digits[:]))
    return rots


def binomial_coefficient(n, k):
    """
    from n positions choose k
    >>> binomial_coefficient(4,2)
    6
    >>> binomial_coefficient(5,3)
    10
    >>> binomial_coefficient(23,10)
    1144066L
    """
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def gen_pandigital_strings(digits):
    """
    >>> [p for p in gen_pandigital_strings("123")]
    ['123', '132', '213', '231', '312', '321']
    >>> s = "12345"
    >>> len([p for p in gen_pandigital_strings(s)]) == reduce(operator.mul, [int(x) for x in s])
    True
    >>> s = "123456789"
    >>> len([p for p in gen_pandigital_strings(s)]) == reduce(operator.mul, [int(x) for x in s])
    True
    """
    for p in itertools.permutations(digits):
        yield "".join(p)


def pentagonal_number(n):
    """
    >>> [pentagonal_number(x) for x in xrange(1, 11)]
    [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    """
    return n * (3 * n - 1) / 2


def triangle_number(n):
    """
    >>> [triangle_number(n) for n in xrange(1,11)]
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """
    return int((float(n) / 2) * (n + 1))


def hexagonal_number(n):
    """
    >>> [hexagonal_number(n) for n in xrange(1,6)]
    [1, 6, 15, 28, 45]
    """
    return n * (2 * n - 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
