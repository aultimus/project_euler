import utils

prime_ceil = 1000000

def main():
    pan_primes = []
    for n in xrange(1, 9):
        s = "".join(str(i) for i in xrange(1, n + 1))
        for pan in utils.gen_pandigital_strings(s):
            if utils.is_prime_cacheless(int(pan)):
                # print pan
                pan_primes.append(int(pan))

    return max(pan_primes)

if __name__ == "__main__":
    print main()
