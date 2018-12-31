text = """473 players; last marble is worth 70904 points"""

players,_,_,_,_,_,points,_ = text.split()
players = int(players)
points = int(points)

class Node :
    def __init__(self, number) :
        self.number = number
        self.clockwise = self
        self.ccw = self
        
    def place(self, number) :
        this = Node(number)
        this.ccw = self.clockwise
        this.clockwise = self.clockwise.clockwise
        self.clockwise.clockwise.ccw = this
        self.clockwise.clockwise = this
        return this
    
    def removeSeventh(self) :
        self.ccw.ccw.ccw.ccw.ccw.ccw.ccw.ccw.clockwise = self.ccw.ccw.ccw.ccw.ccw.ccw
        self.ccw.ccw.ccw.ccw.ccw.ccw.ccw = self.ccw.ccw.ccw.ccw.ccw.ccw.ccw.ccw
        return self.ccw.ccw.ccw.ccw.ccw.ccw
    
    def debug(self) :
        print("[",end='')
        print(self.number,end='')
        this = self.clockwise
        while this != self :
            print(',',this.number,end='')
            this = this.clockwise
        print("]")
        
from itertools import cycle
from itertools import chain

scores = [0] * players

marbles = range(points+1).__iter__()
lowest = marbles.__next__()
circle = Node(lowest)
lowest = marbles.__next__()

for pp in cycle(range(players)) :
    if lowest % 23 == 0 :
        scores[pp] += lowest
        valueOfSeventh = circle.ccw.ccw.ccw.ccw.ccw.ccw.ccw.number
        scores[pp] += valueOfSeventh
        circle = circle.removeSeventh()
    else :
        circle = circle.place(lowest)
    if lowest == points :
        break
    lowest = marbles.__next__()

print(max(scores))
