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
invalid = None
for value in xmas[size:] :
    answer = pairs(value,preamble)
    if answer :
        invalid = answer
    preamble.append(value)
    
contiguous = deque()
print(invalid)
for value in xmas :
    contiguous.append(value)
    while sum(contiguous) > invalid :
        contiguous.popleft()
    if sum(contiguous) == invalid :
        print(min(contiguous)+max(contiguous))
