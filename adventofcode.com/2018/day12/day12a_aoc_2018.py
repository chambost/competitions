puzzleinput = r""""""

pilist = puzzleinput.split("\n")
initial = pilist[0].strip("initial state: ")
grow = dict( x.split(" => ") for x in pilist[2:])

def step(state) :
    global offset
    offset -= 2
    state = state.join(["....","...."])
    newstate = list()
    for ii in range(len(state) - 4) :
        try :
            newstate.append(grow[state[ii:ii+5]])
        except KeyError :
            newstate.append(".")
    return "".join(newstate)
    
def generations(state, num) :
    for ii in range(num) :
        state = step(state)
    return state

def number(state) :
    global offset
    total = 0
    for ii,cell in enumerate(state,start=offset) :
        if cell == "#" :
            total += ii
    return total
    
offset = 0
print(initial)

print(generations(initial,196))

offset = 0

print()
answer = initial
gens = 0
num = number(answer)
answers = [ (gens,num) ]
print(gens,num,answer)
prev = num
for ii in range(1000) :
    gens += 1
    answer = step(answer)
    num = number(answer)
    print(gens,num,prev) # ,answer)
    answers.append((gens,num,num-prev))
    prev = num
print()
print(answers)
print()
