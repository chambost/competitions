puzzleinput = r"""5 9 2 8
9 4 7 3
3 8 6 5"""

count = 0
for values in ([int(v) for v in l.split()] for l in puzzleinput.splitlines()) :
    for v in set(values) :
        for o in set(values) - { v } :
            if float(v//o) == v/o :
                count += v//o
print(count)
