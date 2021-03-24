#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING full_name as parameter.
#

def solve(full_name):
    new_tag = []
    new_tag.append("xXx")
    for name in full_name.split() :
        new_name = []
        for i,c in enumerate(name) :
            new_name.append(c.upper() if i % 2 == 0 else c.lower())
        new_tag.append("".join(new_name))
    new_tag.append("xXx")
    return "_".join(new_tag)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    output = solve(a)

    fptr.write(output + '\n')

    fptr.close()

