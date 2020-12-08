puzzleinput = r"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

acc = 0
inst = 0
program = [line.split() for line in puzzleinput.splitlines()]
seen = [False] * len(program)

def execute(i) :
    global acc
    if seen[i] :
        return acc
    seen[i] = True
    if program[i][0] == "acc" :
        acc += int(program[i][1])
        return execute(i+1)
    if program[i][0] == "jmp" :
        return execute(i+int(program[i][1]))
    if program[i][0] == "nop" :
        return execute(i+1)

print(execute(inst))
