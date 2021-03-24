TT = int(input())
for ii in range(1,1+TT) :
  print("Case #{}: ".format(ii),end="")
  S = input()
  nesting = 0
  for d in (int(x) for x in S) :
    if nesting == d :
      print(d,end="")
    elif nesting < d :
      print("("*(d-nesting),d,sep="",end="")
      nesting = d
    elif nesting > d :
      print(")"*(nesting-d),d,sep="",end="")
      nesting = d
  print(")"*nesting,sep="",end="")
  print()
