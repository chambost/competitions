puzzleinput = r""""""

testinput = r"""Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]
9 1 1 1
9 1 1 2"""

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

choseninput = testinput
firstpart,secondpart = choseninput.split("\n\n\n")
print(len(firstpart))
samples = firstpart.split("\n\n")
count = 0
opcodes = dict()
for 
for sample in samples :
    a,b,c = sample.split("\n") 
    a = [ int(x) for x in a.strip("Before: [").strip("]").split(", ") ]
    b = [ int(x) for x in b.split(" ")]
    c = [ int(x) for x in c.strip("After: [").strip("]").split(", ") ]
    number = sum([ f(a,b) == c for f in functions ])
    count += 1 if number >= 3 else 0
print(count)
