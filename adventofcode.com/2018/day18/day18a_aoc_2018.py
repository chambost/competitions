puzzleinput = r""""""

testinput = r""".#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

def change(ll,this) :
    from collections import Counter
    bag = Counter(ll)
    if this == "." and bag["|"] >= 3 :
        return "|"
    elif this == "|" and bag["#"] >= 3 :
        return "#"
    elif this == "#" :
        if bag["|"] >= 1 and bag["#"] >= 1 :
            return "#"
        else :
            return "."
    return this
    

def solve_day18a_aoc_2018_part_1(choseninput) :
    grid = choseninput.split("\n")
    ww = len(grid[0])
    hh = len(grid)
    
    for ii in range(10000) :
        newgrid = [ [ "." for jj in range(ww)] for kk in range(hh)]
        # corners
        newgrid[0][0] = change((grid[0][1]
                               ,grid[1][1]
                               ,grid[1][0])
                        , grid[0][0])
        newgrid[0][ww-1] = change((grid[0][ww-2]
                                  ,grid[1][ww-2]
                                  ,grid[1][ww-1])
                              , grid[0][ww-1])
        newgrid[hh-1][0] = change((grid[hh-2][0]
                                  ,grid[hh-2][1]
                                  ,grid[hh-1][1])
                              , grid[hh-1][0])
        newgrid[hh-1][ww-1] = change((grid[hh-2][ww-1]
                                     ,grid[hh-2][ww-2]
                                     ,grid[hh-1][ww-2])
                              , grid[hh-1][ww-1])
        #edges
        for jj in range(1,ww-1) :
            newgrid[0][jj] = change((grid[0][jj-1]
                                    ,grid[0][jj+1]
                                    ,grid[1][jj-1]
                                    ,grid[1][jj]
                                    ,grid[1][jj+1])
                                , grid[0][jj])
            newgrid[hh-1][jj] = change((grid[hh-1][jj-1]
                                    ,grid[hh-1][jj+1]
                                    ,grid[hh-2][jj-1]
                                    ,grid[hh-2][jj]
                                    ,grid[hh-2][jj+1])
                                , grid[hh-1][jj])
        for kk in range(1,hh-1) :
            newgrid[kk][0] = change((grid[kk-1][0]
                                    ,grid[kk+1][0]
                                    ,grid[kk-1][1]
                                    ,grid[kk][1]
                                    ,grid[kk+1][1])
                                , grid[kk][0])
            newgrid[kk][ww-1] = change((grid[kk-1][ww-1]
                                    ,grid[kk+1][ww-1]
                                    ,grid[kk-1][ww-2]
                                    ,grid[kk][ww-2]
                                    ,grid[kk+1][ww-2])
                                , grid[kk][ww-1])
        # middle
        for jj in range(1,ww-1) :
            for kk in range(1,hh-1) :
                newgrid[kk][jj] = change((grid[kk-1][jj-1]
                                         ,grid[kk-1][jj]
                                         ,grid[kk-1][jj+1]
                                         ,grid[kk][jj-1]
                                         ,grid[kk][jj+1]
                                         ,grid[kk+1][jj-1]
                                         ,grid[kk+1][jj]
                                         ,grid[kk+1][jj+1])
                                    , grid[kk][jj])
        grid = newgrid
        
    trees = sum((True for xx in range(ww) for yy in range(hh) if grid[yy][xx] == "|" ))
    yards = sum((True for xx in range(ww) for yy in range(hh) if grid[yy][xx] == "#" ))
    return trees*yards   
    
solve_day18a_aoc_2018_part_1(testinput)
