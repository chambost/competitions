puzzleinput = r""""""

def execute(pointer) :
    if codes[pointer] == 1 :
        codes[codes[pointer+3]] = codes[codes[pointer+1]] + codes[codes[pointer+2]]
        return 4
    if codes[pointer] == 2 :
        codes[codes[pointer+3]] = codes[codes[pointer+1]] * codes[codes[pointer+2]]
        return 4
    if codes[pointer] == 99 :
        return 0
    return 0

for noun in range(99) :
    for verb in range(99) :
        codes = [int(v) for v in puzzleinput.split(",")]

        pointer = 0
        codes[1] = noun
        codes[2] = verb
        increment = execute(pointer)
        while increment != 0 :
            pointer += increment
            increment = execute(pointer)
        if codes[0] == 19690720 :
            print(noun * 100 + verb)
