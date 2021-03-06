# http://projecteuler.net/problem=22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?


alphaStart = ord("A") - 1


def score(s, pos):
    return sum([ord(c) - alphaStart for c in s]) * pos

def main():
    nameData = open("names.txt").readline().split(",")
    names = sorted([name.strip('"') for name in nameData])
    return sum([score(name, i + 1) for i, name in enumerate(names)])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print main()
