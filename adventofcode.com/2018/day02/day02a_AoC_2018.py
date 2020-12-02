puzzleinput = r"""bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""

from collections import Counter

twos = 0
threes = 0
for line in puzzleinput.splitlines() :
    bag = Counter(line).values()
    twos += 1 if 2 in bag else 0
    threes += 1 if 3 in bag else 0
print( twos * threes )
