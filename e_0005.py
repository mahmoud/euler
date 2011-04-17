#!/usr/bin/env python

from fractions import gcd
from operator import itemgetter

def ilcm(iterable):
    return reduce(lambda x,y: (x*y)/gcd(x,y), iterable)


if __name__ == "__main__":
    target = range(1,21)
    print ilcm(target)
