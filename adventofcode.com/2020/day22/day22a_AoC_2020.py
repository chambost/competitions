puzzleinput = r"""Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

from collections import deque

one,two = puzzleinput.split("\n\n")
head1,stack1 = one.split(":\n")
deck1 = deque((int(n) for n in stack1.splitlines()))
head2,stack2 = two.split(":\n")
deck2 = deque((int(n) for n in stack2.splitlines()))
def playround() :
    left = deck1.popleft()
    right = deck2.popleft()
    if left > right :
        deck1.append(left)
        deck1.append(right)
    else :
        deck2.append(right)
        deck2.append(left)
while len(deck1) != 0 and len(deck2) != 0 :
    playround()
count = 0
if len(deck2) == 0 :
    while len(deck1) > 0 :
        count += len(deck1) * deck1.popleft()
else :
    while len(deck2) > 0 :
        count += len(deck2) * deck2.popleft()
print(count)
