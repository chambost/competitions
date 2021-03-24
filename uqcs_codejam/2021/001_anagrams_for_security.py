#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isItAnAnagram' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING command
#  2. STRING check
#

def isItAnAnagram(command, check):    
    from collections import Counter
    difference = Counter(command)
    difference.subtract(Counter(check))
    for elem,count in difference.items() :
        if count < 0 :
            return 0
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    agatha = first_multiple_input[0]

    me = first_multiple_input[1]

    isAnagram = isItAnAnagram(agatha, me)

    fptr.write(str(int(isAnagram)) + '\n')

    fptr.close()
