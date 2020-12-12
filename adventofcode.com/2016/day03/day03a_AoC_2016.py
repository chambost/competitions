puzzleinput = r"""5 10 25"""

count = 0
for line in puzzleinput.splitlines() :
    a,b,c = [int(x) for x in line.split()]
    if a+b>c and a+c>b and b+c>a :
        count += 1
print(count)
