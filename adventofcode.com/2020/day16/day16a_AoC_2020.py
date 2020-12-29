puzzleinput = r"""class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

first,second,third = puzzleinput.split("\n\n")
valid = set()
for line in first.splitlines() :
    left,right = line.split(": ")
    range1,range2 = right.split(" or ")
    min,max = (int(n) for n in range1.split("-"))
    for i in range(min,max+1) :
        valid.add(i)
    min,max = (int(n) for n in range2.split("-"))
    for i in range(min,max+1) :
        valid.add(i)
invalid_count = 0
for line in third.splitlines()[1:] :
    for n in (int(x) for x in line.split(",")) :
        if n not in valid :
            invalid_count += n
print(invalid_count)
