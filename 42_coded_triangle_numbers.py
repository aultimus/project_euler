import doctest
import utils

t_nums = set([utils.triangle_number(x) for x in xrange(1, 1000)])


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

def main():
    with open("p042_words.txt") as f:
        words = [word.lower().strip('"') for word in f.read().split(",")]

    t_words = [word for word in words if is_triangle_word(word)]
    return len(t_words)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
