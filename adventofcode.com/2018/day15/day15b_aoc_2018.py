
puzzleinput = r""""""

testinput0 = r"""#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""

testinput1 = r"""#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

testinput2 = r"""#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

testinput3 = r"""#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""

testinput4 = r"""#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""

testinput5 = r"""#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""

choseninput = puzzleinput
elfattack = 24

from itertools import chain

goblins = []
elves = []
dungeon = [ [ Cell(yy,xx,cell) for xx,cell in enumerate(line) ] for yy,line in enumerate(choseninput.split("\n")) ]


reading_order = lambda yy,xx : ((-1+yy,xx),(yy,-1+xx),(yy,1+xx),(1+yy,xx))
contains = lambda yy,xx,unittype : (yy,xx) in ( (u.yy,u.xx) for u in unittype if not u.dead )
contains_goblin = lambda yy,xx : contains(yy,xx,goblins)
contains_elf = lambda yy,xx : contains(yy,xx,elves)
contains_unit = lambda yy,xx : contains_goblin(yy,xx) or contains_elf(yy,xx)
vacant = lambda yy,xx : not contains_unit(yy,xx) and dungeon[yy][xx].cc != "#"

living_count = lambda enemies : sum((True for u in enemies if not u.dead))

from collections import deque
def shortest(start,targets) :
    options = deque([[start]])
    seen = set([start])
    while options :
        nextpath = options.popleft()
        yy,xx = nextpath[-1]
        if (yy,xx) in targets :
            return nextpath
        for y2,x2 in reading_order(yy,xx)  :
            if vacant(y2,x2) and (y2,x2) not in seen :

                options.append(nextpath + [(y2,x2)])
                seen.add((y2,x2))
    return []

for yy,row in enumerate(dungeon) :
    for xx,cell in enumerate(row) :
        if cell.cc == "G" :
            goblins.append( Unit(yy,xx,elves,3) )
            dungeon[yy][xx].cc = "."
        if cell.cc == "E" :
            elves.append( Unit(yy,xx,goblins,elfattack))
            dungeon[yy][xx].cc = "."
            
units = list(chain(goblins,elves))
def battle() :
    rounds = 0
    while True :
        units.sort()
        for u in units :
            if living_count(u.enemies) == 0 :
                return rounds
            u.move()
        rounds += 1
        
rounds = battle()
       
print("Elf attack")
print(elfattack)
print("Dead elf count")
print(sum((True for u in elves if u.dead)))
print()
    
print(rounds)
print(sum((u.hp for u in units if u.hp > 0)))
print(rounds * sum((u.hp for u in units if u.hp > 0)))

for u in units :
     print(u.dead,u.hp,"E" if u.enemies == goblins else "G",u.yy,u.xx)
