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

choseninput = testinput0

class Cell() :
    def __init__(self,yy,xx,cc) :
        self.yy = yy
        self.xx = xx
        self.cc = cc
        self.north = None
        self.west = None
        self.east = None
        self.south = None

    def __lt__(self,other) :
        return self.yy < other.yy or self.yy == other.yy and self.xx < other.xx 
        
from itertools import chain

goblins = []
elves = []
dungeon = [ [ Cell(yy,xx,cell) for xx,cell in enumerate(line) ] for yy,line in enumerate(choseninput.split("\n")) ]


reading_order = lambda yy,xx : ((-1+yy,xx),(yy,-1+xx),(yy,1+xx),(1+yy,xx))
contains = lambda yy,xx,unittype : (yy,xx) in ( (u.yy,u.xx) for u in unittype if not u.dead )
contains_goblin = lambda yy,xx : contains(yy,xx,goblins)
contains_elf = lambda yy,xx : contains(yy,xx,elves)
#contains_elf = lambda xx,yy : (xx,yy) in ( (u.xx,u.yy) for u in elves if not u.dead )
contains_unit = lambda yy,xx : contains_goblin(yy,xx) or contains_elf(yy,xx)
vacant = lambda yy,xx : not contains_unit(yy,xx) and dungeon[yy][xx].cc != "#"

living_count = lambda enemies : sum((True for u in enemies if not u.dead))
# living_goblin_count = lambda : sum((True for u in goblins if not u.dead))
# living_elf_count = lambda : sum((True for u in elves if not u.dead))

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
#            if 0 <= x2 < width and 0 <= y2 < height and vacant(x2,y2) and (x2,y2) not in seen :
            if vacant(y2,x2) and (y2,x2) not in seen :

                options.append(nextpath + [(y2,x2)])
                seen.add((y2,x2))
    return []
    
from itertools import compress

class Unit() :
    def __init__(self,yy,xx,enemies) :
        self.yy = yy
        self.xx = xx
        self.enemies = enemies
        self.atk = 3
        self.hp = 200
        self.dead = False
        
    def move(self) :
        if self.dead :
            return
        if any( contains(yy,xx,self.enemies) for yy,xx in reading_order(self.yy,self.xx) ) :
            self.attack()
            return
        targets = ( (enemy.yy,enemy.xx) for enemy in self.enemies if not enemy.dead )
        in_range = chain.from_iterable( ( reading_order(*coord) for coord in targets ) )
        #in_dungeon = [ (xx,yy) for xx,yy in in_range if 0 <= xx < width and 0 <= yy < height ]
        free = [ (yy,xx) for yy,xx in in_range if vacant(yy,xx) ]
        ranges = [ len(shortest((self.yy,self.xx),(target,))) for target in free ]
        try :
            least = min((r for r in ranges if r != 0))
        except ValueError :
            return
        closest = list(compress(free,(r == least for r in ranges)))
        if len(closest) == 0 :
            return
        closest.sort()
        chosen = closest[0]
        self.yy,self.xx = shortest((self.yy,self.xx),(chosen,))[1]

        self.attack()
        
    def attack(self) :
        if self.dead :
            return
        if not any( contains(yy,xx,self.enemies) for yy,xx in reading_order(self.yy,self.xx) ) :
            return 
        neighbours = [ e for e in self.enemies if (e.yy,e.xx) in reading_order(self.yy,self.xx) and not e.dead]
        lowesthp = min(( e.hp for e in neighbours ))
        lowhp = [ e for e in neighbours if e.hp == lowesthp ]
        lowhp.sort()
        target = lowhp[0]
        target.hp -= self.atk
        if target.hp <= 0 :
            target.dead = True
        
    def __lt__(self,other) :
        return self.yy < other.yy or self.yy == other.yy and self.xx < other.xx 
        
        
height = len(dungeon)
width = len(dungeon[0])

for yy,row in enumerate(dungeon) :
    for xx,cell in enumerate(row) :
        if cell.cc == "G" :
            goblins.append( Unit(yy,xx,elves) )
            dungeon[yy][xx].cc = "."
        if cell.cc == "E" :
            elves.append( Unit(yy,xx,goblins))
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
        
print(rounds)
print(sum((u.hp for u in units if u.hp > 0)))
print(rounds * sum((u.hp for u in units if u.hp > 0)))

for u in units :
     print(u.dead,u.hp,"E" if u.enemies == goblins else "G",u.yy,u.xx)
     
