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
    counter = Counter(group)
    del counter['\n']
    count += len(counter.items())
print(count)
