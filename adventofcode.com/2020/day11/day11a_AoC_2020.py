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

def num_occupied(grid,r,c) :
    count = 0
    if r not in {0} :
        if c not in {0} :
            if grid[r-1][c-1] in {"#"} :
                count += 1
        if c not in {len(grid[0])-1} :
            if grid[r-1][c+1] in {"#"} :
                count += 1
        if grid[r-1][c] in {"#"} :
            count += 1
    if r not in {len(grid)-1} :
        if c not in {0} :
            if grid[r+1][c-1] in {"#"} :
                count += 1
        if c not in {len(grid[0])-1} :
            if grid[r+1][c+1] in {"#"} :
                count += 1
        if grid[r+1][c] in {"#"} :
            count += 1
    if c not in {0} :
        if grid[r][c-1] in {"#"} :
            count += 1
    if c not in {len(grid[0])-1} :
        if grid[r][c+1] in {"#"} :
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
                if num_occupied(grid,r,c) >= 4:
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
            
