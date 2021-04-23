TT = int(input())
for t in range(1,1+TT) :
    NN = int(input())
    SS = input()
    numbers = [1]
    count = 1
    for n in range(1,NN) :
        if ord(SS[n]) > ord(SS[n-1]) :
            count += 1
        else:
            count = 1
        numbers.append(count)
    answer = " ".join(str(x) for x in numbers)
    print(f"Case #{t}: {answer}")
