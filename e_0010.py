#!/usr/bin/env python

from operator import add
from util import primes

if __name__ == "__main__":
    target = 2000000
    primes_lt_target = primes.filter_lt(target)

    print reduce(add, primes_lt_target)
