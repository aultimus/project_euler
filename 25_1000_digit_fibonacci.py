# http://projecteuler.net/problem=25
# The Fibonacci sequence is defined by the recurrence relation:
#
#   Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

# Recursive fibonacci is going to give us a stack overflow, use iterative

def main():
    x, y = 1, 1
    n = x + y
    count = 2
    while len(str(n)) < 1000:
        n = x + y
        x, y = y, n
        count += 1
    return count

if __name__ == "__main__":
    print main()
