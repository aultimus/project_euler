# https://projecteuler.net/problem=24
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, #2, 3 and 4. If all of the
# permutations are listed numerically or alphabetically, we call it
# lexicographic order. #The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools


def get_lexographical_permutations(n):
    """
    Yields permutations on string n.
    >>> [p for p in get_lexographical_rotations("012")]
    ["012", "021", "102", "120", "201", "210"]
    """
    for perm in itertools.permutations(n):
        yield ''.join(perm)

def main():
    for c, p in enumerate(get_lexographical_permutations("0123456789")):
        if c == 1000000 - 1:  # counting from 0
            return p

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
