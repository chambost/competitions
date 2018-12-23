def solve_day09a_aoc_2018(text) :
    players,_,_,_,_,_,points,_ = text.split()
    players = int(players)
    points = int(points)

    class Node :
        def __init__(self, number) :
            self.number = number
            self.clockwise = self
            self.ccw = self

        def place(self, number) :
            second = self.clockwise
            third = self.clockwise.clockwise

            this = Node(number)
            this.ccw = second
            this.clockwise = third
            second.clockwise = this
            third.ccw = this
            return this

        def removeSeventh(self) :
            eighth = self.ccw.ccw.ccw.ccw.ccw.ccw.ccw.ccw
            sixth  = self.ccw.ccw.ccw.ccw.ccw.ccw

            eighth.clockwise = sixth
            sixth.ccw = eighth
            return sixth

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

    return max(scores)

