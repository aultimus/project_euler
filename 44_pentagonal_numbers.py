# https://projecteuler.net/problem=44
#
# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten
# pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
# 70 - 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
# difference are pentagonal and D = |Pk - Pj| is minimised; what is the
# value of D?

import utils

limit = 10000  # limit in our search for pentagonal nums to prevent hangs

def main():
    p = [utils.pentagonal_number(n) for n in xrange(1, limit)]
    p_set = set(p)  # for fast lookups

    # p_k > p_j as p_k - p_j must be pentagonal ie. positive
    return min([p[k] - p[j] for k in xrange(0, len(p)) for j in xrange(0, k)
               if p[k] + p[j] in p_set and p[k] - p[j] in p_set])


# the long way:
# d = 100000000  # our smallest pentagonal difference
# for k in xrange(0, len(p_nums)):
#     # progress print
#     if not k % 1000:
#         print k
#     p_k = p_nums[k]
#     # p_k > p_j as p_k - p_j must be pentagonal ie. positive
#     for j in xrange(0, k):
#         p_j = p_nums[j]
#         diff = p_k - p_j
#         if p_j + p_k in p_nums_set and diff in p_nums_set:
#             print "found valid pentagonal pair %d and %d" % (p_j, p_k)
#             if diff < d:
#                 d = diff
#                 print("p_j %d and p_k %d produce smallest diff so far: %d"
#                     % (p_j, p_k, d))


if __name__ == "__main__":
    print main()
