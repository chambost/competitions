puzzleinput = r"""abc

a
b
c

ab
ac

a
a
a
a

b"""

from collections import Counter

count = 0
for group in puzzleinput.split("\n\n") :
    number = len(group.split("\n"))
    counter = Counter(group)
    del counter['\n']
    for item,n in counter.items() :
        if n == number :
            count += 1
print(count)
