def invert(AA) :
    inverted = list()
    for a in AA :
        if a == "T" :
            inverted.append("F")
        else :
            inverted.append("T")
    return "".join(inverted)
    
TT = int(input())
for t in range(1,1+TT) :
    NN, QQ = (int(x) for x in input().split())
    if NN == 1 :
        AA, SS = input().split()
        SS = int(SS)
        if SS > QQ - SS :
            print(f"Case #{t}: {AA} {SS}/1")
        else : 
            print(f"Case #{t}: {invert(AA)} {QQ-SS}/1")
    if NN == 2 :
        AA1, SS1 = input().split()
        SS1 = int(SS1)
        AA2, SS2 = input().split()
        SS2 = int(SS2)
        if QQ - SS1 > SS1 :
            AA1 = invert(AA1)
            SS1 = QQ - SS1
        if QQ - SS2 > SS2 :
            AA2 = invert(AA2)
            SS2 = QQ - SS2
        if SS1 > SS2 :
            print(f"Case #{t}: {AA1} {SS1}/1")
        else :
            print(f"Case #{t}: {AA2} {SS2}/1")
            
            
