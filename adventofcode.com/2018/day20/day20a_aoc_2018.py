puzzleinput = r""""""
testinput0 = r"""^WNE$"""
testinput1 = r"""^ENWWW(NEEE|SSE(EE|N))$"""
testinput2 = r"""^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"""
testinput3 = r"""^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""
testinput4 = r"""^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""

class Room() :
    def __init__(self) :
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.number = -1
    
    def paint(self,first) :
        from collections import deque
        bfs = deque([(self,first)])
        maxn = 0
        while len(bfs) > 0 :
            nextroom,n = bfs.popleft()
            maxn = max(maxn,n)
            nextroom.number = n
            for room in nextroom.unpainted_rooms() :
                bfs.append((room,n+1))
        return maxn
        
    def thousandpaint(self,first) :
        from collections import deque
        bfs = deque([(self,first)])
        maxn = 0
        count = 0
        while len(bfs) > 0 :
            nextroom,n = bfs.popleft()
            maxn = max(maxn,n)
            if nextroom.number == -1 :
                nextroom.number = n
                if n >= 1000 :
                    count += 1
                for room in nextroom.unpainted_rooms() :
                    bfs.append((room,n+1))
        return count
        
    def rooms(self) :
        return ( room for room in ( self.south , self.west, self.north , self.east ) if room )

    def unpainted_rooms(self) :
        return ( room for room in ( self.south , self.west, self.north , self.east ) if room and room.number == -1 )    
    
    def sn(self, other) :
        self.north = other
        other.south = self
        
    def we(self, other) :
        self.east = other
        other.west = self
        
    def S(self) :
        if not self.south :
            other = Room()
            other.sn(self)
        return self.south
    
    def N(self) :
        if not self.north :
            other = Room()
            self.sn(other)
        return self.north
    
    def W(self) :
        if not self.west :
            other = Room()
            other.we(self)
        return self.west
    
    def E(self) :
        if not self.east :
            other = Room()
            self.we(other)
        return self.east
        
def solve_day20a_aoc_2018(choseninput) :
    
    def navigate(first,future) :
        last = first
        try :
            while True :
                c = future.popleft()
                if (c == "(") :
                    last = navigate(last,future)
                elif (c == "|") :
                    last = first
                elif (c == ")") :
                    return last
                else :
                    last = getattr(last,c)()
        except IndexError :
            pass
        return last
        
    from collections import deque
    
    start = Room()
    navigate(start, deque(choseninput.strip("^").strip("$")))
    
    return start.paint(0)
        
print( solve_day20a_aoc_2018(testinput0) )
print( solve_day20a_aoc_2018(testinput1) )
print( solve_day20a_aoc_2018(testinput2) )
print( solve_day20a_aoc_2018(testinput3) )
print( solve_day20a_aoc_2018(testinput4) )


print( solve_day20a_aoc_2018(puzzleinput) )
