#!/usr/bin/env python

from math import sqrt
from util import primes

if __name__ == "__main__":
    target = 600851475143
    factor_candidates = primes.filter_lt(int(sqrt(target)))

    factors = [ x for x in factor_candidates if target % x == 0 ]
    print factors[-1]
