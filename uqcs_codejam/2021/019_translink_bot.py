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
# The function accepts following parameters:
#  1. STRING station
#  2. STRING line
#  3. STRING_ARRAY stations
#  4. STRING_ARRAY express
#

def solve(station, line, stations, express):
    # Write your code here
    first = f"This is a {line} train, "
    if len(express) == 0 :
        second = "stopping all stations. "
    else :
        print(express)
        new_stations = []
        start = True
        middle = True
        end = False
        for s in stations :
            if end :
                new_stations.append(s)
            if not start and s == express[-1] :
                end = True
            if start and s != express[0] :
                new_stations.append(s)
            elif s == express[0] :
                start = False
            if not start and not end and middle :
                for e in express :
                    new_stations.append(e)
                middle = False
        stations = new_stations
        if len(express) == 2 :
            second = f"running express from {express[0]} to {express[-1]}. "
        if len(express) == 3 :
            second = f"running express from {express[0]} to {express[-1]}, stopping only at {express[1]}. "
        if len(express) == 4 :
            second = f"running express from {express[0]} to {express[-1]}, stopping only at {express[1]} and {express[2]}. "
        if len(express) > 4 :
            second = f"running express from {express[0]} to {express[-1]}, stopping only at "
            for e in express[1:-2] :
                second += f"{e}, "
            second += f"and {express[-2]}. " 
    third = f"The next station is {stations[stations.index(station)+1]}."
    return first + second + third

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    l = input()

    n = int(input().strip())

    ss = []

    for _ in range(n):
        ss_item = input()
        ss.append(ss_item)

    x = int(input().strip())

    xs = []

    for _ in range(x):
        xs_item = input()
        xs.append(xs_item)

    output = solve(s, l, ss, xs)

    fptr.write(output + '\n')

    fptr.close()

