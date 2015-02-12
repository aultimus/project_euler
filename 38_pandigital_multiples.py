import utils

def main():
    pans = [p for p in utils.gen_pandigital_strings("123456789")]
    mult_pans = []

    for n in xrange(2, 20):
        for i in xrange(1,100000):
            concat = "".join([str(i * x) for x in xrange(1, n + 1)])
            if len(concat) == 9 and concat in pans:
                mult_pans.append(int(concat))
    return max(mult_pans)

if __name__ == "__main__":
    print main()
