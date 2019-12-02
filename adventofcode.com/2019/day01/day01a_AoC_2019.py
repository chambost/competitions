puzzleinput = r""""""

solve_one = lambda x : (x // 3) - 2
solve = lambda x : sum(solve_one(int(a)) for a in x.split())
print(solve(puzzleinput))
