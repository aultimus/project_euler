import doctest


def triangle_number(n):
    """
    >>> [triangle_number(n) for n in xrange(1,11)]
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """
    return int((float(n) / 2) * (n + 1))


t_nums = set([triangle_number(x) for x in xrange(1, 1000)])


def is_triangle_word(s):
    """
    >>> is_triangle_word("sky")
    True
    """
    t_val = word_triangle_value(s)
    if t_val > max(t_nums):
        raise ValueError("t_nums not large enough")
    return t_val in t_nums


def word_triangle_value(word):
    """
    >>> word_triangle_value("sky")
    55
    """
    base = ord("a") - 1
    return sum([ord(c) - base for c in word])


doctest.testmod()

with open("p042_words.txt") as f:
    words = [word.lower().strip('"') for word in f.read().split(",")]

t_words = [word for word in words if is_triangle_word(word)]
print len(t_words)
