import math
import time

def main():
    result = 0, 0
    for p in xrange(120, 1000):
        num_sols = 0
        for a in xrange(1, p / 4):
            for b in xrange(a + 1, (p - a) / 2):
                c = math.sqrt(a ** 2 + b ** 2)
                if a + b + c == p:
                    num_sols += 1
        if num_sols > result[1]:
            result = p, num_sols
    return result[0]

if __name__ == "__main__":
    start = time.time()
    print main()
    print "took", time.time() - start, "seconds"
