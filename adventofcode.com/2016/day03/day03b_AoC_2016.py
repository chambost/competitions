puzzleinput = r""""""

def valid(a,b,c) :
    if a+b>c and a+c>b and b+c>a :
        return 1
    return 0
count = 0
lines = iter(puzzleinput.splitlines())
for first,second,third in zip(lines, lines, lines) :
    a,d,g = [int(x) for x in first.split()]
    b,e,h = [int(x) for x in second.split()]
    c,f,i = [int(x) for x in third.split()]
    count += valid(a,b,c)
    count += valid(d,e,f)
    count += valid(g,h,i)
print(count)
