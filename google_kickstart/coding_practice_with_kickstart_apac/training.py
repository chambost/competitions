def coaching(target,index,ss,pp) :
    total = 0
    for i in range(index+1,index+pp) :
        total += target - ss[i]
    return total

TT = int(input())
for t in range(1,1+TT) :
    NN, PP = (int(x) for x in input().split())
    SS = sorted([int(x) for x in input().split()],reverse=True)
    answer = 10000 * NN
    for i,s in enumerate(SS) :
        if i <= NN - PP :
            answer = min(coaching(s,i,SS,PP),answer)
    print(f"Case #{t}: {answer}")
