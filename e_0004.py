#!/usr/bin/env python

from util import is_palindrome
if __name__ == "__main__":
    cur_max_xy = 0
    max_x      = 0
    max_y      = 0
    for x in xrange(100, 1000):
        for y in xrange(100, 1000):
            res = x*y
            if is_palindrome(res) and res > cur_max_xy:
                max_x = x
                max_y = y
                cur_max_xy = res

    print 'x:',max_x
    print 'y:',max_y
    print 'max pali:',cur_max_xy
