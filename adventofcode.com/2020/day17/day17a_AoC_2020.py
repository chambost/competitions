puzzleinput = r""".#.
..#
###"""

from collections import Counter

cubes = set()
for row,line in enumerate(puzzleinput.splitlines()) :
    for column,char in enumerate(line) :
        if char == "#" :
            cubes.add((row,column,0))
for i in range(6) :
    counts = Counter()
    for r,c,d in cubes :
        counts[(r-1,c-1,d-1)] += 1
        counts[(r-1,c-1,d)] += 1
        counts[(r-1,c-1,d+1)] += 1
        counts[(r-1,c,d-1)] += 1
        counts[(r-1,c,d)] += 1
        counts[(r-1,c,d+1)] += 1
        counts[(r-1,c+1,d-1)] += 1
        counts[(r-1,c+1,d)] += 1
        counts[(r-1,c+1,d+1)] += 1
        counts[(r,c-1,d-1)] += 1
        counts[(r,c-1,d)] += 1
        counts[(r,c-1,d+1)] += 1
        counts[(r,c,d-1)] += 1
    #    counts[(r,c,d)] += 1
        counts[(r,c,d+1)] += 1
        counts[(r,c+1,d-1)] += 1
        counts[(r,c+1,d)] += 1
        counts[(r,c+1,d+1)] += 1
        counts[(r+1,c-1,d-1)] += 1
        counts[(r+1,c-1,d)] += 1
        counts[(r+1,c-1,d+1)] += 1
        counts[(r+1,c,d-1)] += 1
        counts[(r+1,c,d)] += 1
        counts[(r+1,c,d+1)] += 1
        counts[(r+1,c+1,d-1)] += 1
        counts[(r+1,c+1,d)] += 1
        counts[(r+1,c+1,d+1)] += 1
    new_cubes = set()
    for loc,count in counts.items() :
        if loc in cubes and count in (2,3) :
            new_cubes.add(loc)
        if loc not in cubes and count == 3 :
            new_cubes.add(loc)
    cubes = new_cubes
print(len(cubes))
