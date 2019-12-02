puzzleinput = r""""""

solve_one = lambda x : (x // 3) - 2

count = 0
for a in (int(x) for x in puzzleinput.split()) :
  this = solve_one(a)
  while (this >= -2) :
    count += this if this > 0 else 0
    this = solve_one(this)
print(count)
