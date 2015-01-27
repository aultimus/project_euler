import doctest
import utils

pans = [p for p in utils.gen_pandigital_strings("123456789")]
products = []

for pan in pans:
    for i in xrange(1, len(pan)):
        for j in xrange(i + 1, len(pan)):
            m1, m2, product = pan[:i], pan[i:j], pan[j:]
            # print m1, m2, product
            if int(m1) * int(m2) == int(product):
                print m1, "*", m2, "=", product
                products.append(int(product))
print sum(set(products))
