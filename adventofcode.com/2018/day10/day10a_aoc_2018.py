stars = r""""""

stars = stars.split("\n")
stars = [ x.split("> ") for x in stars ]
stars = [ [x.strip("position=<"),y.strip("velocity=<").strip(">")] for x,y in stars ]
stars = [ [x.split(", "),y.split(", ")] for x,y in stars ]
stars = [ [ [ int(x) for x in y] for y in _] for _ in stars]

def step(n) :
    global pxs
    global pys
    global t
    pxs = [ pxs[i]+n*vxs[i] for i in range(len(pxs)) ]
    pys = [ pys[i]+n*vys[i] for i in range(len(pys)) ]
    t += n
    print( t,max(pxs)-min(pxs),max(pys)-min(pys) )
    
pxs = [ x for x,y in [ a for a,b in stars ] ]
pys = [ y for x,y in [ a for a,b in stars ] ]
vxs = [ x for x,y in [ b for a,b in stars ] ]
vys = [ y for x,y in [ b for a,b in stars ] ]
t = 0

step(10867)
pxs = [ x-min(pxs) for x in pxs ]
pys = [ y-min(pys) for y in pys ]
grid = [ [ "." for x in range(1+max(pxs)-min(pxs))] for y in range(1+max(pys)-min(pys)) ]

for i in range(len(pxs)) :
    grid[pys[i]][pxs[i]] = "#"

for g in grid :
    print( "".join(g) )

print(pxs)
print(pys)

for i in range(10) : 
    step(1000)
for i in range(8) :
    step(100)
for i in range(10) :
    step(-1)
for i in range(100) :
    step(1)



