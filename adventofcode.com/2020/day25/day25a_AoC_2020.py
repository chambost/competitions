puzzleinput = r"""5764801
17807724"""

a,b = (int(n) for n in puzzleinput.splitlines())
loop1 = 0
subject = 7
current = subject
while True:
    loop1 += 1
    current *= subject
    current %= 20201227
    if current == a :
        break
print(loop1)
loop2 = 0
subject = 7
current = subject
while True:
    loop2 += 1
    current *= subject
    current %= 20201227
    if current == b :
        break
print(loop2)
subject = a
current = a
for n in range(loop2) :
    current *= subject
    current %= 20201227
print(current)
