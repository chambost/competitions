puzzleinput = r""""""

testinput0 = r"""pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""

def solve_day23a_aoc_2018(choseninput) :
    nanobot_input = choseninput.split("\n")
    nanobots = []
    for nanobot in nanobot_input :
        first,second = nanobot.split(", ")
        x,y,z = ( int(_) for _ in first.strip("pos=<").strip(">").split(",") )
        r = int( second.strip("r="))
        nanobots.append((r,z,y,x))
    nanobots.sort()
    strongest = nanobots.pop()
    count = 1
    for nanobot in nanobots :
        count += 1 if abs(nanobot[1]-strongest[1])+abs(nanobot[2]-strongest[2])+abs(nanobot[3]-strongest[3]) <= strongest[0] else 0    
    return count
    
solve_day23a_aoc_2018(testinput0)
