# http://projecteuler.net/problem=16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


def main():
    n = 2 ** 1000
    l = str(n)
    l = [int(v) for v in l]
    return sum(l)

if __name__ == "__main__":
    print main()
