#!/usr/bin/env python

from itertools import takewhile

def fib_gen():
    x, y = 1, 1
    while True:
       x, y = y, x+y
       yield x

if __name__ == "__main__":
    print sum( [i for i in 
                takewhile(lambda x: x<4000000,fib_gen()) 
                if i % 2 == 0])

