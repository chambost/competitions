puzzleinput = r"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

program = [line.split() for line in puzzleinput.splitlines()]
seen = [False] * len(program)

def execute(i,acc,seen,changed) :
    print(i,acc)
    if i == len(program) :
        return False,acc
    if seen[i] :
        return True,acc
    seen[i] = True
    if program[i][0] == "acc" :
        acc += int(program[i][1])
        return execute(i+1,acc,seen.copy(),changed)
    if program[i][0] == "jmp" :
        if changed :
            return execute(i+int(program[i][1]),acc,seen.copy(),changed)
        else :
            early,a = execute(i+1,acc,seen.copy(),True)
            if early :
                return execute(i+int(program[i][1]),acc,seen.copy(),changed)
            else :
                return early,a
    if program[i][0] == "nop" :
        if changed :
            return execute(i+1,acc,seen.copy(),changed)
        else :
            early,a = execute(i+int(program[i][1]),acc,seen.copy(),True)
            if early :
                return execute(i+1,acc,seen.copy(),changed)
            else :
                return early,a

print(execute(0,0,seen,False))
