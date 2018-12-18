xs = []
ys = []

try :
  while True :
    x,y = [ int(_) for _ in raw_input().split(", ") ]
    xs.append(x)
    ys.append(y)
except EOFError :
  pass

max_x = max(xs)
max_y = max(ys)
grid = [ [ -1 for y in range(max_y) ] for x in range(max_x) ]

def taxicab(a,b,x,y) :
  return abs(a-x) + abs(b-y)

def total(x,y) :
  total = 0
  for ii in range(len(xs)) :
    total += taxicab(x,y,xs[ii],ys[ii])
  return total 

for x in range(max_x) :
  for y in range(max_y) :
    grid[x][y] = total(x,y)

allregions = sum([ 1 if s < 10000 else 0 for t in grid for s in t ])

newgrid = [[ 1 if s < 10000 else 0 for s in t ] for t in grid ]

sizes = []

def calc(x,y) :
  newnewgrid = [[ 0 for s in t ] for t in grid ]
  newnewgrid[x][y] = 1

  old = 0
  current = 1
  def paint(x,y) :
    if newnewgrid[x][y] == 0 :
      newnewgrid[x][y] = 1 if newgrid[x][y] else 0

  def repaint() :
    for x in range(max_x) :
      for y in range(max_y) :
        if newnewgrid[x][y] == 1 :
          if x > 0 :
            paint(x-1,y)
          if x < max_x - 1 :
            paint(x+1,y)
          if y > 0 :
            paint(x,y-1)
          if y < max_y - 1 :
            paint(x,y+1)
  while old != current :
    old = sum([ s for t in newnewgrid for s in t ])
    repaint()
    current = sum([ s for t in newnewgrid for s in t ])
  for x in range(max_x) :
    for y in range(max_y) :
      if newnewgrid[x][y] == 1 :
        newgrid[x][y] = 0
  return current

for x in range(max_x) :
  for y in range(max_y) :
    if newgrid[x][y] == 1 :
      sizes.append(  calc(x,y) )

print( sum(sizes) )
