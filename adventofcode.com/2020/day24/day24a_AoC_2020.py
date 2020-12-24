puzzleinput = r"""sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

from collections import deque
from collections import Counter

def parseline(line) :
    d = deque(line)
    while d :
        first = d.popleft()
        if first in {"s","n"} :
            second = d.popleft()
            yield "".join((first,second))
        else :
            yield first
            
def removeopposites(c) :
    if c["w"] > c["e"] :
        c["w"] -= c["e"]
        c["e"] -= c["e"]
    else :
        c["e"] -= c["w"]
        c["w"] -= c["w"]
    if c["sw"] > c["ne"] :
        c["sw"] -= c["ne"]
        c["ne"] -= c["ne"]
    else :
        c["ne"] -= c["sw"]
        c["sw"] -= c["sw"]
    if c["nw"] > c["se"] :
        c["nw"] -= c["se"]
        c["se"] -= c["se"]
    else :
        c["se"] -= c["nw"]
        c["nw"] -= c["nw"]
        
def removeloops(c) :
    changed = True
    while changed :
        changed = False
        if c["w"] > 0 and c["ne"] > 0 and c["se"] > 0 :
            m = min(c["w"],c["ne"],c["se"])
            c["w"] -= m
            c["ne"] -= m
            c["se"] -= m
            changed = True
        if c["e"] > 0 and c["nw"] > 0 and c["sw"] > 0 :
            m = min(c["e"],c["nw"],c["sw"])
            c["e"] -= m
            c["nw"] -= m
            c["sw"] -= m
            changed = True
            
def shorten(c) :
    if c["se"] > 0 and c["w"] > 0 :
        m = min(c["se"],c["w"])
        c["se"] -= m
        c["w"] -= m
        c["sw"] += m
    if c["nw"] > 0 and c["sw"] > 0 :
        m = min(c["nw"],c["sw"])
        c["nw"] -= m
        c["sw"] -= m
        c["w"] += m
    if c["ne"] > 0 and c["w"] > 0 :
        m = min(c["ne"],c["w"])
        c["ne"] -= m
        c["w"] -= m
        c["nw"] += m
    if c["nw"] > 0 and c["e"] > 0 :
        m = min(c["nw"],c["e"])
        c["nw"] -= m
        c["e"] -= m
        c["ne"] += m
    if c["ne"] > 0 and c["se"] > 0 :
        m = min(c["ne"],c["se"])
        c["ne"] -= m
        c["se"] -= m
        c["e"] += m
    if c["e"] > 0 and c["sw"] > 0 :
        m = min(c["e"],c["sw"])
        c["e"] -= m
        c["sw"] -= m
        c["se"] += m

bag = Counter()
for line in puzzleinput.splitlines() :
    c = Counter(parseline(line))
    removeopposites(c)
    removeloops(c)
    shorten(c)
    bag[tuple(sorted(c.elements()))] += 1
count = 0
for v in bag.values() :
    count += (v % 2)
print(count)
