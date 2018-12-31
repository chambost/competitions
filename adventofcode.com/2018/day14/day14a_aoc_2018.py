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
        
def stringize(listofints) :
    return "".join( ( str(ii) for ii in listofints ) )
    
def solve(target) :
    global scoreboard
    while True :
        step()
        if len(scoreboard) >= 10 + target :
            return stringize(scoreboard[target:10+target])
            
print(solve(int(testinput)))
