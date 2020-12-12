puzzleinput = r"""F10
N3
F7
R90
F11"""

directions = [(1,0),(0,1),(-1,0),(0,-1)]
def move(loc,wp,action,value) :
    if action == "N" :
        return loc,(wp[0],wp[1]-value)
    if action == "S" :
        return loc,(wp[0],wp[1]+value)
    if action == "E" :
        return loc,(wp[0]+value,wp[1])
    if action == "W" :
        return loc,(wp[0]-value,wp[1])
    if action == "L" :
        if (value // 90) == 1 :
            return loc,(wp[1],-wp[0])
        if (value // 90) == 2 :
            return loc,(-wp[0],-wp[1])
        if (value // 90) == 3 :
            return loc,(-wp[1],wp[0])
    if action == "R" :
        if (value // 90)  == 1 :
            return loc,(-wp[1],wp[0])
        if (value // 90) == 2 :
            return loc,(-wp[0],-wp[1])
        if (value // 90) == 3 :
            return loc,(wp[1],-wp[0])
    if action == "F" :
        return (loc[0]+value*wp[0],loc[1]+value*wp[1]),wp
    return loc,wp
loc = (0,0)
wp = (10,-1)
for line in puzzleinput.splitlines() :
    action = line[:1]
    value = int(line[1:])
    loc,wp = move(loc,wp,action,value)
    
print(abs(loc[0])+abs(loc[1]))
