puzzleinput = r"""389125467"""

def destination(first,cups) :
    while True:
        if first < min(cups) :
            return max(cups)
        first -= 1
        if first in cups :
            return first

def iterate(cups) :
    first = cups.popleft()
    second = cups.popleft()
    third = cups.popleft()
    fourth = cups.popleft()
    cups.append(first)
    d = destination(first,cups)
    i = cups.index(d)
    cups.insert(i+1, fourth)
    cups.insert(i+1, third)
    cups.insert(i+1, second)
    
cups = deque((int(n) for n in puzzleinput))
for i in range(100) :
    iterate(cups)
print(cups)
