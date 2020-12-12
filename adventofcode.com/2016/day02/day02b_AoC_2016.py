puzzleinput = r"""ULL
RRDDD
LURDL
UUUUD"""

def relocate(position,move) :
    if move == "U" :
        if position == 3 :
            return 1
        if position in { 6 , 7 , 8 } :
            return position - 4
        if position == "A" :
            return 6
        if position == "B" :
            return 7
        if position == "C" :
            return 8
        if position == "D" :
            return "B"
    if move == "D" :
        if position == 1 :
            return 3
        if position in { 2 , 3 , 4 } :
            return position + 4
        if position == 6 :
            return "A"
        if position == 7 :
            return "B"
        if position == 8 :
            return "C"
        if position == "B" :
            return "D"
    if move == "L" :
        if position in { 3 , 4 , 6 , 7 , 8 , 9 } :
            return position - 1
        if position == "B" :
            return "A"
        if position == "C" :
            return "B"
    if move == "R" :
        if position in { 2 , 3 , 5 , 6 , 7 , 8 } :
            return position + 1
        if position == "A" :
            return "B"
        if position == "B" :
            return "C"
    return position

position = 5
answer = []
for line in puzzleinput.splitlines() :
    for move in line :
        position = relocate(position,move)
    answer.append(str(position))
print("".join(answer))
