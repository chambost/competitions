#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'based' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER inputBase
#  4. INTEGER outputBase
#

def int2base(x, base):
    import string
    digs = string.digits + string.ascii_letters
    
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

def based(a, b, inputBase, outputBase):
    # Write your code here
    difference = int(str(a),inputBase) - int(str(b),inputBase)
    return int2base(difference,outputBase)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    unused = int(input().strip())

    x1 = int(input().strip())

    x2 = int(input().strip())

    inBase = int(input().strip())

    outBase = int(input().strip())

    val = based(x1, x2, inBase, outBase)

    fptr.write(str(val) + '\n')

    fptr.close()

