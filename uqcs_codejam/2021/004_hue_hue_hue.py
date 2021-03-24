#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY rgb
#

def solve(N, rgb):
    rs,gs,bs = zip(*rgb)
    return sum(rs)//N,sum(gs)//N,sum(bs)//N
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    output = solve(n, arr)

    fptr.write(' '.join(map(str, output)))
    fptr.write('\n')

    fptr.close()

