#!/usr/bin/env python

from itertools import product 
# could use, but list compies are more readable.
# the code below does take about 8-12 seconds though

if __name__ == "__main__":
    print [ (x,y,z,x*y*z) 
            for x in xrange(1,1001) 
            for y in xrange(x,1001) 
            for z in xrange(y,1001) 
            if x+y+z == 1000 
            and x**2 + y**2 == z**2 ][0]
