puzzleinput = r"""5 1 9 5
7 5 3
2 4 6 8"""

count = 0
for values in ([int(v) for v in l.split()] for l in puzzleinput.splitlines()) :
    count += max(values) - min(values)
print(count)
