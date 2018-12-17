puzzleinput = r""""""

testinput = r"""x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504"""

def solve_day17a_aoc_2018(choseninput) :

    from collections import defaultdict

    pressure = defaultdict(lambda : False)
    for line in choseninput.split("\n") :
        first,second = line.split(", ")
        x1,x2 = 0,0
        y1,y2 = 0,0
        for text in ( first , second ) :
            if text[0] == "x" :
                text = text.strip("x=")
                if ".." in text :
                    x1,x2 = ( int(_) for _ in text.split("..") )
                    x2 += 1
                else :
                    x1 = int(text)
                    x2 = 1 + x1
            else :
                text = text.strip("y=")
                if ".." in text :
                    y1,y2 = ( int(_) for _ in text.split("..") )
                    y2 += 1
                else :
                    y1 = int(text)
                    y2 = 1 + y1            
        for x in range(x1,x2) :
            for y in range(y1,y2) :
                pressure[(y,x)] = True

    xs = [ x for y,x in pressure.keys() ]
    ys = [ y for y,x in pressure.keys() ]
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)
    
    if minx > 500 or maxx < 500 :
        return 1 + maxy - miny
    
    start = (-1 + miny,500)
    
    water = defaultdict( lambda : False )
    leftpressure = defaultdict( lambda : False )
    rightpressure = defaultdict( lambda : False )
    halfpressure = defaultdict( lambda : False )
    
    def search(start) :
        from collections import deque
        firsty,firstx = start
        chains = deque([(start,(1+firsty,firstx),start)])
        while chains :
            depthfirstcoord,direction,pressurisehere = chains.popleft()
            yy,xx = depthfirstcoord
            here = (yy,xx)
            up = (-1+yy,xx)
            down = (1+yy,xx)
            twodown = (2+yy,xx)
            left = (yy,-1+xx)
            twoleft = (yy,-2+xx)
            right = (yy,1+xx)
            tworight = (yy,2+xx)
            twodirection = (yy+2*(direction[0]-yy),xx+2*(direction[1]-xx))
        
            if pressure[here] :
                if direction == left :
                    leftpressure[pressurisehere] = True
                elif direction == right :
                    rightpressure[pressurisehere] = True
                continue
            elif not water[here] :
                water[here] = True
                if not pressure[down] :
                    if not 1+yy > maxy and not water[down] :
                        chains.appendleft((here,direction,pressurisehere))
                        chains.appendleft((down,twodown,pressurisehere))
                    elif water[down] and direction != down and not water[direction] :
                        chains.appendleft((here,direction,pressurisehere))
                        chains.appendleft((direction,twodirection,pressurisehere))
                # pressure[down]
#                 elif direction != down and pressure[direction] :
#                     pressure[pressurisehere] = True
                elif direction != down and water[direction] :                
                    pass
                else :             
                    chains.appendleft((here,direction,pressurisehere))
                    chains.appendleft((direction,twodirection,pressurisehere))
            # (backflow) water[here]
            elif not pressure[down] :
                continue # flow back without pressure
            # pressure[down]
            elif direction != down :
                if halfpressure[here] :
                    pressure[here] = True
                    if not pressure[direction] :
                        chains.appendleft((direction,twodirection,pressurisehere))
                elif pressure[direction] or halfpressure[direction] :
                    halfpressure[here] = True
                elif not water[direction] :                
                    chains.appendleft((here,direction,pressurisehere))
                    chains.appendleft((direction,twodirection,pressurisehere))
            elif direction == down :
                if pressure[left] and pressure[right] :
                    pressure[here] = True
                elif pressure[right] and halfpressure[left] :
                    chains.appendleft((here,direction,pressurisehere))
                    chains.appendleft((left,twoleft,here))                    
                elif pressure[left] and halfpressure[right] :
                    chains.appendleft((here,direction,pressurisehere))
                    chains.appendleft((right,tworight,here))
                elif halfpressure[left] and halfpressure[right] :
                    chains.appendleft((here,direction,pressurisehere))
                    chains.appendleft((left,twoleft,here))                    
                    chains.appendleft((right,tworight,here))
                elif (water[left] or pressure[left]) and (water[right] or pressure[right]) :
                    pass
                else :
                    chains.appendleft((here,direction,pressurisehere))
                    chains.appendleft((left,twoleft,here))
                    chains.appendleft((right,tworight,here))

    search(start)
    
    count = 0
    for yy,xx in [a for a,b in water.items() if b and pressure[a]] :
        if miny<=yy<=maxy :
            count += 1
    return count

print( solve_day17a_aoc_2018(testinput) )

# print( solve_day17a_aoc_2018(puzzleinput) )
