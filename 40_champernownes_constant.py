# https://projecteuler.net/problem=40

ceil = 1000000

def main():
    # A gig of memory, that's one helluva string
    l = [str(i) for i in xrange(0, 1000000)]
    s = "".join(l)
    indexes = [1, 10, 100, 1000,
               10000, 100000, 1000000]
    return reduce(lambda x, y: x * y, [int(s[i]) for i in indexes])

if __name__ == "__main__":
    print main()
