TT = int(input())
for t in range(1,1+TT) :
    NN = int(input())
    XX = [int(x) for x in input().split()]
    operations = 0
    for n in range(NN-1) :
        if XX[n+1] <= XX[n] :
            count = XX[n] + 1
            while str(count)[:len(str(XX[n+1]))] != str(XX[n+1]) :
                count += 1
            operations += len(str(count)) - len(str(XX[n+1]))
            XX[n+1] = count
    print(f"Case #{t}: {operations}")
