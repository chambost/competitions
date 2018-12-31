
testinput = r"""37"""
scoreboard = [ int(x) for x in testinput ]
original_len = len(scoreboard)
elfindices = [ int(x) for x in range(2)]
elves = [ scoreboard[ei] for ei in elfindices]

def digitsofsum() :
    global elves
    return [ int(x) for x in str(sum(elves)) ]

def step() :
    global scoreboard
    global elves
    global elfindices
    scoreboard.extend( digitsofsum() )
    new_len = len(scoreboard)
    for ii,elfindex in enumerate(elfindices) :
        elfindices[ii] = (elfindex + scoreboard[elfindex] + 1) % new_len
        elves[ii] = scoreboard[elfindices[ii]]
        
def stringize(listofints, start) :
    return "".join( ( str(ii) for ii in listofints[start:] ) )
    
def solve() :
    global scoreboard
    start = 0
    threshold = 10
    while True :
        step()
        try :
            return start + stringize(scoreboard, start).index(testinput)
        except ValueError :
            pass
        if len(scoreboard) >= threshold :
            print(len(scoreboard))
            threshold *= 10
        start = len(scoreboard) - 6
        
print(solve())
