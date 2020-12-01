puzzleinput = r"""R8, R4, R4, R8"""
#puzzleinput = r""""""

N = 0
E = 1
S = 2
W = 3
directions = ((1,0), (0,1), (-1,0), (0,-1))
loc = (0,0)
dir = N

def turn(dir,angle) :
  dir += 1 if angle == "R" else -1
  dir %= len(directions)
  return dir
  

def step(loc,face,z) :
  return (loc[0] + z * face[0], loc[1] + z * face[1])

visited = set()
visited.add(loc)

for angle,z in ((step[0],int(step[1:])) for step in puzzleinput.split(", ")) :
  dir = turn(dir,angle)
  for x in range(z) :
    loc = step(loc,directions[dir],1)
    if loc in visited :
        print(sum(abs(x) for x in loc))
        break
    visited.add(loc)
  else :
    continue
  break
