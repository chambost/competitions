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
# The function accepts 2D_INTEGER_ARRAY table as parameter.
#

def solve(table):
    columns = zip(*table)
    answer = []
    for c in columns :
        differences = [t - s for s,t in zip(c,c[1:])]
        if all(d == 0 for d in differences) :
            answer.append('E')
        elif all(d < 0 for d in differences) :
            answer.append('D')
        elif all(d > 0 for d in differences) :
            answer.append('A')
        else :
            answer.append('-')
    return answer
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    R = int(first_multiple_input[0])

    C = int(first_multiple_input[1])

    data = []

    for _ in range(R):
        data.append(list(map(int, input().rstrip().split())))

    result = solve(data)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

