
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
    """
    def mark(x):
        for i in xrange(x*2,len(n),x):
            n[i][1] = 0
    # Add actual integer vals for readability rather than using indexes
    # [number, marked]
    n = [[i, 1] for i in range(2, c)]
    p = 2
    marked = False
    for e in n:
        if not marked:
            yield p
            mark(p)
            marked = True
        if e[0] > p and e[1]:
            p = e[0]
            marked = False

def isPrime(n):
    for i in xrange(2, n):
        if n % i == 0:
            return False
    return True

def trialDivision(n, printAsWeGo=True):
    primeFactors = []
    for i in xrange(2, n):
        if n % i == 0 and isPrime(i):
            primeFactors.append(i)
            if printAsWeGo:
                print i
    return primeFactors