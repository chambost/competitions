TT = int(input())
for t in range(1,1+TT) :
    NN, BB = (int(x) for x in input().split())
    AA = [int(x) for x in input().split()]
    count = 0
    tally = 0
    for a in sorted(AA) :
        tally += a
        if tally <= BB :
            count += 1
    print(f"Case #{t}: {count}")
