from itertools import ifilter, takewhile
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

# for testin!    
def get_composites(li):
    return [x for x in li if not is_prime(x)]

def modulo_test(t):
    return lambda x: x%t != 0

def count(i=0, step=1):
    while True:
        #if i == 11:
        #    import pdb; pdb.set_trace()
        val = (yield i)
        if val is not None:
            i = val
        else:
            i += step

def filter_lt(top):
    i = 0
    t = 3 #skip 2, add it at the end                                                                      
    p = xrange(t, top, 2)
    primes = [t]
    toproot = sqrt(top)
    try:
        while t < toproot:
            p = ifilter(modulo_test(t), p)
            t = p.next()
            primes.append(t)
            i += 1
        primes.extend(list(p))
    except StopIteration as s:
        #print i
        pass
    primes.insert(0,2)
    return primes

def takewhile(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break

def prime_list(length):
    t = 3
    p = count(t, 2) # skip 2 add it at the end
    primes = [2, 3]
    i = 1
    while len(primes) < length:
        p = ifilter(modulo_0_not_square(t), p) # see note below
        primes.extend(takewhile(tw(t), p))
        i += 1
        t = primes[i]
    # print i # iterations
    # print len(primes) # cap out for this number of iterations
    return primes[:length]

# This is used because takewhile will take care of removing the square
# for us. The square is sort of like the bumper that lets us know we're
# done taking.
def modulo_0_not_square(t):
    return lambda x: x%t != 0 or x == t**2

def tw(t):
    return lambda x: x < t**2

