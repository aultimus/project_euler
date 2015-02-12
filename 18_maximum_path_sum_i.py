# Optimisation: Use more memory efficient data structure than string

def gen_all_n_length_bitsrings(n):
    """
    >>> [x for x in gen_all_n_length_bitsrings(3)]
    ['000', '001', '010', '011', '100', '101', '110', '111']
    """
    for i in range(1 << n):
        yield '{:0{}b}'.format(i, n)


def take_path(data, directions):
    """
    >>> data = [[3], [7, 4], [2, 4, 6], [8, 5 , 9, 3]]
    >>> take_path(data, "001") == 3 + 7 + 2 + 5
    True
    >>> take_path(data, "101") == 3 + 4 + 4 + 9
    True
    >>> take_path(data, "011") == 3 + 7 + 4 + 9
    True
    """
    assert(len(directions) == len(data) - 1)
    cur_pos = 0
    vals = []
    for i in xrange(0, len(data)):
        if i == 0:
            d = 0
        else:
            d = int(directions[i - 1])
        cur_pos += d
        vals.append(data[i][cur_pos])
    # print vals
    return sum(vals)

def main():
    with open("18_max_path_sum_i_data.txt") as f:
        data = [[int(x) for x in line.strip().split()]
                for line in f.readlines() if line]

    # Brute force approach
    return max([take_path(data, p) for p in gen_all_n_length_bitsrings(len(data) - 1)])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
