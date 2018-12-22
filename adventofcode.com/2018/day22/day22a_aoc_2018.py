puzzleinput = r""""""

testinput0 = r"""depth: 510
target: 10,10"""

def solve_day22a_aoc_2018(choseninput) :
    first,second = choseninput.split("\n")
    depth = int(first.strip("depth: "))
    tx,ty = ( int(x) for x in second.strip("target: ").split(",") )
    
    from functools import lru_cache
    
    @lru_cache(maxsize=(tx+1)*(ty+1))
    def geologic_index(y,x) :
        if (y,x) == (0,0) :
            return 0
        elif (y,x) == (ty,tx) :
            return 0
        elif y == 0 :
            return x * 16807
        elif x == 0 :
            return y * 48271
        return erosion_level(y,x-1) * erosion_level(y-1,x)
    
    @lru_cache(maxsize=(tx+1)*(ty+1))    
    def erosion_level(y,x) :
        return (geologic_index(y,x) + depth) % 20183
    
    def risk(y,x) :
        return erosion_level(y,x) % 3
    
    answer = 0
    for ii in range(ty+1) :
        for jj in range(tx+1) :
            answer += risk(ii,jj)

    return answer
    
solve_day22a_aoc_2018(testinput0)

solve_day22a_aoc_2018(puzzleinput)
