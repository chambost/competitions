puzzleinput = r"""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

from collections import deque

def pairs(value,preamble) :
    def pair_found() :
        for a in set(preamble) :
            for b in set(preamble) - {a} :
                if a+b == value :
                    return True
        return False
    if not pair_found() :
        return value
    return None
    
xmas = [int(x) for x in puzzleinput.splitlines()]
size = 5
preamble = deque(xmas[:size],size)
for value in xmas[size:] :
    answer = pairs(value,preamble)
    if answer :
        print(answer)
    preamble.append(value)
