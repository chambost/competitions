#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findTheSpecialTwo' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY names
#  2. INTEGER_ARRAY scores
#  3. INTEGER specialValue
#

def findTheSpecialTwo(names, scores, specialValue):
    lookup = dict(zip(scores,names))
    for v,n in lookup.items() :
        other = specialValue - v
        if other != v and other in lookup :
            return n, lookup[other]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ns = input().rstrip().split()

    xs = list(map(int, input().rstrip().split()))

    s = int(input().strip())

    theSpecialTwo = findTheSpecialTwo(ns, xs, s)

    fptr.write(' '.join(theSpecialTwo))
    fptr.write('\n')

    fptr.close()
