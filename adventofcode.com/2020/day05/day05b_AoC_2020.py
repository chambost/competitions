puzzleinput = r""""""

numbers = []
for b in puzzleinput.splitlines() :
    b = b.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    numbers.append(int(b,2))
for n in sorted(numbers) :
    print(n)
