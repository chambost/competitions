puzzleinput = r""""""

testinput0 = r"""depth: 510
target: 10,10"""

def solve_day22b_aoc_2018(choseninput) :
    first,second = choseninput.split("\n")
    depth = int(first.strip("depth: "))
    tx,ty = ( int(x) for x in second.strip("target: ").split(",") )
    
    from functools import lru_cache
    
    @lru_cache(maxsize=(tx*tx+1)*(depth+1))
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
    
    @lru_cache(maxsize=(tx*tx+1)*(depth+1))
    def erosion_level(y,x) :
        return (geologic_index(y,x) + depth) % 20183
    
    def risk(y,x) :
        return erosion_level(y,x) % 3
    
    def nextareas(y,x) :
        if (y,x) == (0,0) :
            return ((1,0),(0,1))
        elif y == 0 :
            return ((0,x-1),(1,x),(0,x+1))
        elif x == 0 :
            return ((y-1,0),(y,1),(y+1,0))
        else :
            return ((y-1,x),(y,x-1),(y+1,x),(y,x+1))
    
    from collections import defaultdict
    
    answers = dict()
    torch_ans = dict()
    climbing_ans = dict()
    neither_ans = dict()
    equip = dict()
    possibilities = defaultdict( lambda : [] )
    times = defaultdict( lambda : [] )
    
    times[0].append((0,0,1))
    
    rocky = 0
    wet = 1
    narrow = 2
    
    neither = 0
    torch = 1
    climbing = 2

    t = 0
    y,x = (0,0)
    
    def answer_check(cy,cx,e) :
        if e == neither :
            return (cy,cx) in neither_ans
        elif e == torch :
            return (cy,cx) in torch_ans
        else :
            return (cy,cx) in climbing_ans
        
    def answer_add(cy,cx,e,t) :
        answers[(cy,cx)] = t
        if e == neither :
            neither_ans[(cy,cx)] = t
        elif e == torch :
            torch_ans[(cy,cx)] = t
        else :
            climbing_ans[(cy,cx)] = t
        
    
    while True :
        while times[t] :
            cy,cx,e = times[t].pop()
            if not answer_check(cy,cx,e) :
                answer_add(cy,cx,e,t)
                if (cy,cx) == (ty,tx) and e == torch :
                    return t
                if not (cy,cx) in neither_ans and risk(cy,cx) != rocky :
                    times[t+7].append((cy,cx,neither))
                if not (cy,cx) in torch_ans and risk(cy,cx) != wet :
                    times[t+7].append((cy,cx,torch))
                if not (cy,cx) in climbing_ans and risk(cy,cx) != narrow :
                    times[t+7].append((cy,cx,climbing))                    
                for ny,nx in nextareas(cy,cx) :
                    if answer_check(ny,nx,e) :
                        pass
                    elif risk(ny,nx) == rocky and e != neither :
                        times[t+1].append((ny,nx,e))
                    elif risk(ny,nx) == wet and e != torch :
                        times[t+1].append((ny,nx,e))
                    elif risk(ny,nx) == narrow and e != climbing : # narrow # elif risk(ny,nx) == narrow and
                        times[t+1].append((ny,nx,e))
        del times[t]
        t = min(times.keys())        
        
solve_day22b_aoc_2018(testinput0)

solve_day22b_aoc_2018(puzzleinput)
