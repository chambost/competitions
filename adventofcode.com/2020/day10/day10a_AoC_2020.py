puzzleinput = r"""16
10
15
5
1
11
7
19
6
12
4"""

#puzzleinput = r"""28
#33
#18
#42
#31
#14
#46
#20
#48
#47
#24
#23
#49
#45
#19
#38
#39
#11
#1
#32
#25
#35
#8
#17
#7
#9
#4
#2
#34
#10
#3"""


ones = 0
threes = 1
prev = 0
for x in sorted([int(n) for n in puzzleinput.splitlines()]) :
    if x - prev == 1 :
        ones += 1
    if x - prev == 3 :
        threes += 1
    prev = x
print(ones,threes,ones*threes)
