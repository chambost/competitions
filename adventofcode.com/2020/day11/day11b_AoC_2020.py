puzzleinput = r"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def occupied_dir(grid,r,c,dr,dc) :
    r += dr
    c += dc
    while 0 <= r < len(grid) and 0 <= c < len(grid[0]) :
        if grid[r][c] == "#" :
            return True
        if grid[r][c] == "L" :
            return False
        r += dr
        c += dc
    return False
    

def num_occupied(grid,r,c) :
    count = 0
    for dr,dc in [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(+1,-1),(+1,0),(+1,+1)] :
        if occupied_dir(grid,r,c,dr,dc) :
            count += 1
    return count

grid = [[x for x in line] for line in (puzzleinput.splitlines())]
def iterate() :
    global grid
    newgrid = [["." for x in range(len(grid[0]))] for x in range(len(grid))]
    changed = False
    for r in range(len(grid)) :
        for c in range(len(grid[0])) :
            if grid[r][c] == "L" :
                if num_occupied(grid,r,c) == 0:
                    changed = True
                    newgrid[r][c] = "#"
                else :
                    newgrid[r][c] = "L"
            if grid[r][c] == "#" :
                if num_occupied(grid,r,c) >= 5:
                    changed = True
                    newgrid[r][c] = "L"
                else :
                    newgrid[r][c] = "#"
    grid = newgrid
    return changed
while iterate() :
    pass
count = 0
for row in grid :
    for seat in row :
        if seat == "#" :
            count += 1
print(count)
