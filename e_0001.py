#!/usr/bin/env python

if __name__ == "__main__":
    print sum([ i for i in xrange(0, 999) if i % 3 == 0 or i % 5 == 0])
