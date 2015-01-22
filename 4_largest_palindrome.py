# http://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(s):
    for i in xrange(len(s)/2):
        endInd = i + 1
        if s[i] != s[-endInd]:
            return False
    return True

vals = []
for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        n = i * j
        s = str(n)
        if isPalindrome(s):
            vals.append(n)
print max(vals)
