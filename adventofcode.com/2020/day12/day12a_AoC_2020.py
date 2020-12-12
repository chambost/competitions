puzzleinput = r"""F10
N3
F7
R90
F11"""

directions = [(1,0),(0,1),(-1,0),(0,-1)]
def move(loc,dir,action,value) :
    if action == "N" :
        return (loc[0],loc[1]-value),dir
    if action == "S" :
        return (loc[0],loc[1]+value),dir
    if action == "E" :
        return (loc[0]+value,loc[1]),dir
    if action == "W" :
        return (loc[0]-value,loc[1]),dir
    if action == "L" :
        return loc,(dir-(value//90))%len(directions)
    if action == "R" :
        return loc,(dir+(value//90))%len(directions)
    if action == "F" :
        return (loc[0]+value*directions[dir][0],loc[1]+value*directions[dir][1]),dir
    return loc,dir
dir = 0
loc = (0,0)
for line in puzzleinput.splitlines() :
    action = line[:1]
    value = int(line[1:])
    loc,dir = move(loc,dir,action,value)
    
print(abs(loc[0])+abs(loc[1]))
