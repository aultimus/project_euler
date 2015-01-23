# https://projecteuler.net/problem=19
# You are given the following information, but you may prefer to do some
# research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a
#     century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
#

import datetime # datetime seems like cheating but makes it easier, why not

def is_sunday(d):
    """
    >>>is_sunday(datetime(1900, 1, 8))
    True
    """
    return d.isoweekday() == 7

# 01/01/1901 -> 31/12/2000
# Bruteforce approach
sunday_count = 0
date = datetime.date(1901,1,1)
while date.year < 2001:
    if is_sunday(date) and date.day == 1:
        sunday_count += 1
    date += datetime.timedelta(days=1)

print sunday_count


# I wonder why this doesn't work:
# sunday_count = 0
# for y in xrange(1900, 2001):
#     for m in xrange(1, 13):
#         d = datetime.date(y, m, 1)
#         s = is_sunday(d)
#         if s:
#             print d
#             sunday_count += 1
# print sunday_count
