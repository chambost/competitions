puzzleinput = r""""""

def addr(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]  ] 
    z[y[3]] = x[y[1]] + x[y[2]]
    return z

def addi(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]] + y[2]
    return z

def mulr(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]] * x[y[2]]
    return z

def muli(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]] * y[2]
    return z

def banr(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]] & x[y[2]]
    return z

def bani(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]] & y[2]
    return z

def borr(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]] | x[y[2]]
    return z

def bori(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]] | y[2]
    return z

def setr(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = x[y[1]]
    return z

def seti(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = y[1]
    return z

def gtir(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = 1 if y[1] > x[y[2]] else 0
    return z

def gtri(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5]   ] 
    z[y[3]] = 1 if x[y[1]] > y[2] else 0
    return z

def gtrr(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5] ] 
    z[y[3]] = 1 if x[y[1]] > x[y[2]] else 0
    return z

def eqir(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5] ] 
    z[y[3]] = 1 if y[1] == x[y[2]] else 0
    return z

def eqri(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5] ] 
    z[y[3]] = 1 if x[y[1]] == y[2] else 0
    return z

def eqrr(x,y) :
    z = [ x[0], x[1], x[2], x[3], x[4], x[5] ] 
    z[y[3]] = 1 if x[y[1]] == x[y[2]] else 0
    return z

def solve_day21a_aoc_2018(choseninput) :
    first,second = choseninput.split("\n",maxsplit=1)
    ip = int( first.strip("#ip ") )
    instructions = [] 
    for x in second.split("\n") :
        a,b,c,d = x.split(" ") 
        instructions.append( ( a , int(b), int(c), int(d)))
    registers = [0] * 6
    while registers[ip] < len(instructions) :
        registers = globals()[instructions[registers[ip]][0]](registers,instructions[registers[ip]])
        if registers[ip] == 28 :
            break
        registers[ip] += 1
    return registers[3]
    
solve_day21a_aoc_2018(puzzleinput)
    
    
