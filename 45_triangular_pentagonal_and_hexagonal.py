import utils

limit = 1000000

t_nums = set([utils.triangle_number(x)   for x in xrange(limit)])
p_nums = set([utils.pentagonal_number(x) for x in xrange(limit)])
h_nums = set([utils.hexagonal_number(x)  for x in xrange(limit)])

tph_nums = t_nums.intersection(p_nums).intersection(h_nums)
assert 40755 in tph_nums
print min([n for n in tph_nums if n > 40755])
