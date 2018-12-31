serial = 5177

cells = [ [ 0 for i in range(300+1) ] for j in range(300+1) ]
for y,row in enumerate(cells) :
    if y == 0 :
        continue
    for x,cell in enumerate(row) :
        if x == 0 : 
            continue
        rackid = x + 10
        level = rackid * y
        level += serial
        level *= rackid
        answer = (level // 100) % 10
        answer -= 5
        cells[y][x] = answer
        
def total(x,y) :
    return cells[y][x]   + cells[y+1][x]   + cells[y+2][x] \
         + cells[y][x+1] + cells[y+1][x+1] + cells[y+2][x+1] \
         + cells[y][x+2] + cells[y+2][x+2] + cells[y+2][x+2]
powers = [ (total(x,y),x,y) for x in range(1,300-1) for y in range(1,300-1) ]

from collections import Counter
c = Counter([p for p,_,_ in powers])
maxp = max(c)
print(max(c))

print([(x,y) for p,x,y in powers if p == maxp])

print(len(powers))
print((300-2)*(300-2))

print(max(powers))
print(min(powers))
print(c)

coords = powers.index(max(powers))
print(coords)
print(coords % 300-2)
print(coords // 300-2)
print(total(236,22))


def total(x,y,n) :
    return sum([ cells[y+j][x+i] for j in range(n) for i in range(n)])
max = 0
current = (0,0,0)
for n in range(1,300) :
    print(n)
    for x in range(1,302-n) :
        for y in range(1,302-n) : 
            this = total(x,y,n)
            if this > max :
                print((x,y,n))
                max = this
                current = (x,y,n)
                
