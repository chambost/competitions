fabric = [ [ 0 for x in range(1000) ] for y in range(1000) ]

try :
  while True :
    _,_,corner,size = raw_input().split()
    x,y = [ int(_) for _ in corner.strip(":").split(",") ]
    w,h = [ int(_) for _ in size.split("x") ]
    for i in range(w) :
      for j in range(h) :
        fabric[x+i][y+j] += 1
except EOFError :
  pass
count = 0
for i in range(1000) :
  for j in range(1000) :
    count += 1 if fabric[i][j] >= 2 else 0

print count
