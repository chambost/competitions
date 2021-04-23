TT = int(input())
for t in range(1,1+TT) :
    NN, PP = (int(x) for x in input().split())
    prefixes = [input() for _ in range(PP)]
    filtered_prefixes = []
    for p in prefixes :
        safe = True
        for a in set(prefixes) - {p} :
            if p[:len(a)] == a :
                safe = False
        if safe :
            filtered_prefixes.append(p)
    answer = 2 ** NN
    for f in filtered_prefixes :
        answer -= 2 ** (NN - len(f))
    print(f"Case #{t}: {answer}")
