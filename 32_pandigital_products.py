import utils

products = []

def main():
    for pan in utils.gen_pandigital_strings("123456789"):
        for i in xrange(1, len(pan)):
            for j in xrange(i + 1, len(pan)):
                m1, m2, product = pan[:i], pan[i:j], pan[j:]
                # print m1, m2, product
                if int(m1) * int(m2) == int(product):
                    print m1, "*", m2, "=", product
                    products.append(int(product))
    return sum(set(products))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
