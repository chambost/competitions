puzzleinput = r""""""

from itertools import cycle

class Cart() :
    options = ( 0 , 1 , 2 )
    
    def __init__(self,xx,yy,cc) :
        self.xx = xx
        self.yy = yy
        self.cc = cc
        self.nextTurn = cycle(Cart.options).__iter__()
        self.dead = False
        
    def move(self) :
        if self.dead :
            return
        global track
        if self.cc == "<" :
            self.moveLeft()
        elif self.cc == ">" :
            self.moveRight()
        elif self.cc == "^" :
            self.moveUp()
        elif self.cc == "v" :
            self.moveDown()
        
    def moveLeft(self) :
        self.xx -= 1
        path = track[self.yy][self.xx]
        if path == "-" :
            pass
        elif path == "/" :
            self.cc = "v"
        elif path == "\\" :
            self.cc = "^"
        elif path == "+" :
            self.intersection()
            
    def moveRight(self) :
        self.xx += 1
        path = track[self.yy][self.xx]
        if path == "-" :
            pass
        elif path == "/" :
            self.cc = "^"
        elif path == "\\" :
            self.cc = "v"
        elif path == "+" :
            self.intersection()

            
    def moveUp(self) :
        self.yy -= 1
        path = track[self.yy][self.xx]
        if path == "|" :
            pass
        elif path == "/" :
            self.cc = ">"
        elif path == "\\" :
            self.cc = "<"
        elif path == "+" :
            self.intersection()
            
    def moveDown(self) :
        self.yy += 1
        path = track[self.yy][self.xx]
        if path == "|" :
            pass
        elif path == "/" :
            self.cc = "<"
        elif path == "\\" :
            self.cc = ">"
        elif path == "+" :
            self.intersection()

    def intersection(self) :
        lsr = self.nextTurn.__next__()
        if lsr == 0 :
            if self.cc == "<" :
                self.cc = "v"
            elif self.cc == "v" :
                self.cc = ">"
            elif self.cc == ">" :
                self.cc = "^"
            elif self.cc == "^" :
                self.cc = "<"
        elif lsr == 2 :
            if self.cc == "<" :
                self.cc = "^"
            elif self.cc == "^" :
                self.cc = ">"
            elif self.cc == ">" :
                self.cc = "v"
            elif self.cc == "v" :
                self.cc = "<"
                
    def collision(self) :
        if self.dead :
            return False
        global carts 
        for cart in carts :
            if (not cart.dead) and self != cart and self.xx == cart.xx and self.yy == cart.yy :
                self.die()
                self.isDead()
                cart.die()
                cart.isDead()
                return (self.xx,self.yy)
        return False
    
    def die(self) :
        self.dead = True
    
    def isDead(self) :
        return self.dead
    
    def __lt__(self,other) :
        return self.yy < other.yy or self.yy == other.yy and self.xx < other.xx 


track = [ [ cell for cell in line ] for line in puzzleinput.split("\n") ]

print(len(track))
print([len(x) for x in track])
print(max([len(x) for x in track]))

carts = []
for yy,ll in enumerate(track) :
    for xx,cell in enumerate(ll) :
        if cell == "^" or cell == "v":
            track[yy][xx] = "|"
            #cartgrid[yy][xx] = cell
            carts.append( Cart(xx,yy,cell) )
        if cell == "<" or cell == ">" :
            track[yy][xx] = "-"
            #cartgrid[yy][xx] = cell
            carts.append( Cart(xx,yy,cell) )
print(len(carts))

def run() :
    index = 0
    while True :
        index += 1
        carts.sort()
        otherindex = 0
        for cart in carts :
            otherindex += 1
            cart.move()
            cart.collision()
        if 1 == len( [ 0 if cart.dead else 1 for cart in carts] ) :
            for cart in carts :
                if not cart.dead() :
                    return (cart.xx,cart.yy)
print(run())
                    
