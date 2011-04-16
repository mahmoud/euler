#!/usr/bin/env python

from itertools import ifilter 
from math import sqrt

def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number<=1 or number%2==0:
        return False
    check=3
    maxneeded=number
    while check<maxneeded+1:
        maxneeded=number/check
        if number%check==0:
            return False
        check+=2
    return True
    
def get_composites(li):
    return [x for x in li if not is_prime(x)]

"""def ifilter(predicate, iterable):
    # ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
    if predicate is None:
        predicate = bool
        #import pdb; pdb.set_trace()
    for x in iterable:
        print x,
        if predicate(x):
            yield x

def ifilterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        print x,
        if not predicate(x):
            yield x
"""

def modulo_test(t):
    #def funci(x):
    #    return x % t != 0
    return lambda x: x%t != 0

def filter_primes(top):
    i = 0
    t = 3 #skip 2, add it at the end                                                                      
    p = xrange(t, top, 2)
    primes = []
    toproot = sqrt(top)
    try:
        while t < toproot:
            primes.append(t)
            p = ifilter(modulo_test(t), p)
            t = p.next()
            i += 1
        primes.extend(list(p))
    except StopIteration as s:
        print i
    primes.insert(0,2)
    return primes

def iter_primes():
     # an iterator of all numbers between 2 and +infinity
     numbers = itertools.count(2)

     # generate primes forever
     while True:
         # get the first number from the iterator (always a prime)
         prime = numbers.next()
         yield prime

         # this code iteratively builds up a chain of
         # filters...slightly tricky, but ponder it a bit
         numbers = itertools.ifilter(prime.__rmod__, numbers)

#for p in iter_primes():
#    if p > 1000:
#        break
#    print p


if __name__ == "__main__":
    print 'hi'

