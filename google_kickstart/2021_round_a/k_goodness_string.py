def goodness(s, n) :
    score = 0
    for i in range(n//2) :
        score += 1 if s[i] != s[-i-1] else 0
    return score

TT = int(input())
for t in range(1,1+TT) :
    NN, KK = (int(x) for x in input().split())
    SS = input()
    answer = abs(KK - goodness(SS, NN))
    print(f"Case #{t}: {answer}")
