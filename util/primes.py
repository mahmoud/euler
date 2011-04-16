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

def modulo_test(t):
    #def funci(x):
    #    return x % t != 0
    return lambda x: x%t != 0

def filter_lt(top):
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

