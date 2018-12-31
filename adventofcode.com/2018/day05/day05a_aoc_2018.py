letters = r""""""

polymer = [ ord(x) for x in letters ]

answer = []
for unit in polymer :
    if not answer or abs(answer[-1] - unit) != 32 :
        answer.append( unit )
    else :
        answer.pop()
        
len(answer)
