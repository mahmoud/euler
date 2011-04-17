#!/usr/bin/env python

if __name__ == "__main__":
    sum_of_sqs = reduce(lambda x,y: x+y**2, range(1,101))
    sq_of_sums = reduce(lambda x,y: x+y, range(1,101))**2

    print abs(sum_of_sqs - sq_of_sums)
