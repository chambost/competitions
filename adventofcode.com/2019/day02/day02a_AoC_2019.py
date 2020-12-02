puzzleinput = r""""""

codes = [int(v) for v in puzzleinput.split(",")]

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

pointer = 0
codes[1] = 12
codes[2] = 2
increment = execute(pointer)
while increment != 0 :
    pointer += increment
    increment = execute(pointer)
print(codes[0])
