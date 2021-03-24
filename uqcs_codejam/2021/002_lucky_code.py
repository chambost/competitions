#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING text as parameter.
#

def solve(text):
    sum = 0
    for c in text:
        sum += (ord(c.upper()) - ord('A') + 1) % 7
    return sum
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
