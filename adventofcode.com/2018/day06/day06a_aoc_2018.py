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

def shortest(x,y) :
  current = -1
  length = max_x + max_y + 1
  for ii in range(len(xs)) :
    dist = taxicab(x,y,xs[ii],ys[ii])
    if dist < length :
      current = ii
      length = dist
    elif dist == length :
      current = -1
  return current

for x in range(max_x) :
  for y in range(max_y) :
    grid[x][y] = shortest(x,y)

areas = dict()

def area(i) :
  return sum([ 1 if s == i else 0 for t in grid for s in t ])

for ii in range(len(xs)) :
  areas[ii] = area(ii)

for x in range(max_x) :
  try :
    del areas[grid[x][0]]
  except KeyError :
    pass
  try :
    del areas[grid[x][max_y - 1]]
  except KeyError :
    pass
for y in range(max_y) :
  try :
    del areas[grid[0][y]]
  except KeyError :
    pass
  try :
    del areas[grid[0][max_x - 1]]
  except KeyError :
    pass

answers = [ (b,a) for (a,b) in areas.iteritems() ]
answers = sorted( answers )

print(answers[-1][0])
