fabric = [ [ 0 for x in range(1000) ] for y in range(1000) ]

ids = []
xs = []
ys = []
ws = []
hs = []

try :
  while True :
    id,_,corner,size = raw_input().split()
    ids.append(id)
    x,y = [ int(_) for _ in corner.strip(":").split(",") ]
    xs.append(x)
    ys.append(y)
    w,h = [ int(_) for _ in size.split("x") ]
    ws.append(w)
    hs.append(h)
    for i in range(w) :
      for j in range(h) :
        fabric[x+i][y+j] += 1
except EOFError :
  pass

def check(x,y,w,h) :
  for i in range(w) :
    for j in range(h) :
      if fabric[x+i][y+j] >= 2 :
        return False
  return True

for ii in range(len(ids)) :
  if check(xs[ii], ys[ii], ws[ii], hs[ii]) :
    print ids[ii]
    exit()
