#!/usr/bin/env python

from util import primes
from collections import defaultdict
from itertools import permutations 

def rotations(orig):
    yield orig
    cur = orig[-1]+orig[:-1]
    while cur != orig:
        yield cur
        cur = cur[-1]+cur[:-1]

if __name__ == "__main__":
    target = 1000000 # a milli
    comb_count = defaultdict(int)

    circular_set = set()

    pr_set = set(primes.filter_lt(target))
    print 'total primes len:',len(pr_set)
    for i in pr_set:
        rot_set = set([int(x) for x in rotations(str(i))])
        if( rot_set & pr_set == rot_set ):
            circular_set = circular_set | rot_set

        # if you could modify pr_set while iterating over it,
        # you could optimize to not check for other primes 
        # in the current rot_set

    print 'circ primes len:',len(circular_set) 
