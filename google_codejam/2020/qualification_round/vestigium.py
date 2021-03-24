TT = int(input())
for ii in range(1,1+TT) :
    NN = int(input())
    matrix = [ [ int(x) for x in input().split() ] for _ in range(NN) ]
    trace = sum( matrix[x][x] for x in range(NN) )
    rows = sum( set(matrix[x]) != set(range(1,1+NN)) for x in range(NN) )
    transpose = [list(x) for x in zip(*matrix)]
    columns = sum( set(transpose[x]) != set(range(1,1+NN)) for x in range(NN) )
    
    print("Case #{}: {} {} {}".format(ii, trace, rows, columns))
