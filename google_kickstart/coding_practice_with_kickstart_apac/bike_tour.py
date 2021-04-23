TT = int(input())
for t in range(1,1+TT) :
    NN = int(input())
    HH = [int(x) for x in input().split()]
    peaks = 0
    for i in range(1,NN-1) :
        if HH[i] > HH[i-1] and HH[i] > HH[i+1] :
            peaks += 1
    print(f"Case #{t}: {peaks}")
