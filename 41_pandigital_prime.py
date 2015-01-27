import utils

prime_ceil = 1000000

pan_primes = []

for n in xrange(1, 9):
    s = "".join(str(i) for i in xrange(1, n + 1))
    for pan in utils.gen_pandigital_strings(s):
        if utils.is_prime_cacheless(int(pan)):
            # print pan
            pan_primes.append(int(pan))

print "result", max(pan_primes)
