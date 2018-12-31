puzzleinput = r""""""

def addr(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] + x[y[2]]
    return z

def addi(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] + y[2]
    return z

def mulr(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] * x[y[2]]
    return z

def muli(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] * y[2]
    return z

def banr(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] & x[y[2]]
    return z

def bani(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] & y[2]
    return z

def borr(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] | x[y[2]]
    return z

def bori(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]] | y[2]
    return z

def setr(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = x[y[1]]
    return z

def seti(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = y[1]
    return z

def gtir(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = 1 if y[1] > x[y[2]] else 0
    return z

def gtri(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = 1 if x[y[1]] > y[2] else 0
    return z

def gtrr(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = 1 if x[y[1]] > x[y[2]] else 0
    return z

def eqir(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = 1 if y[1] == x[y[2]] else 0
    return z

def eqri(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = 1 if x[y[1]] == y[2] else 0
    return z

def eqrr(x,y) :
    z = [ x[0], x[1], x[2], x[3] ] 
    z[y[3]] = 1 if x[y[1]] == x[y[2]] else 0
    return z

functions = [ addr, addi
            , mulr, muli
            , banr, bani
            , borr, bori
            , setr, seti
            , gtir, gtri, gtrr
            , eqir, eqri, eqrr ]



choseninput = puzzleinput

firstpart,secondpart = choseninput.split("\n\n\n")
print(len(firstpart))
samples = firstpart.split("\n\n")

from collections import defaultdict
opcodes =  [ [True]*16 for ii in range(16) ]

opcodenumbers = set()

for sample in samples :
    a,b,c = sample.split("\n") 
    a = [ int(x) for x in a.strip("Before: [").strip("]").split(", ") ]
    b = [ int(x) for x in b.split(" ")]
    c = [ int(x) for x in c.strip("After: [").strip("]").split(", ") ]
    matches = [ f(a,b) == c for f in functions ]
    opcodes[b[0]] = [ opcodes[b[0]][x] and matches[x] for x in range(16) ]
    opcodenumbers.add(b[0])
for nn in range(16) :
    for ii,oo in enumerate(opcodes) :
        if sum(oo) == 1 :
            ndx = oo.index(True)
            for jj in range(16) :
                if ii != jj :
                    opcodes[jj][ndx] = False
newfunctions = [ lambda : True ] * 16
for nn in range(16) :
    
    ndx = opcodes[nn].index(True)
    newfunctions[nn] = functions[ndx]
registers = [0,0,0,0]
for line in secondpart.strip().split("\n") :
    op,a,b,c = [ int(x) for x in line.split(" ")]
    registers = newfunctions[op](registers,[op,a,b,c])
    
print(registers)
