puzzleinput = r"""ULL
RRDDD
LURDL
UUUUD"""

def relocate(position,move) :
    if move == "U" :
        if position >= 4 :
            return position - 3
    if move == "D" :
        if position <= 6 :
            return position + 3
    if move == "L" :
        if position in { 2 , 3 , 5 , 6 , 8 , 9 } :
            return position - 1
    if move == "R" :
        if position in { 1 , 2 , 4 , 5 , 7 , 8 } :
            return position + 1
    return position

position = 5
answer = []
for line in puzzleinput.splitlines() :
    for move in line :
        position = relocate(position,move)
    answer.append(str(position))
print("".join(answer))
