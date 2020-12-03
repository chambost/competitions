puzzleinput = r""">"""
#puzzleinput = r"""^>v<"""
#puzzleinput = r"""^v^v^v^v^v"""

def deliver(dir,loc) :
    if dir == "^" :
        return (loc[0],loc[1]+1)
    if dir == ">" :
        return (loc[0]+1,loc[1])
    if dir == "v" :
        return (loc[0],loc[1]-1)
    if dir == "<" :
        return (loc[0]-1,loc[1])
    return loc

count = 0
loc = (0,0)
visited = set()
visited.add(loc)
count += 1
for dir in puzzleinput :
    loc = deliver(dir,loc)
    if loc not in visited :
        count += 1
    visited.add(loc)
print(count)
