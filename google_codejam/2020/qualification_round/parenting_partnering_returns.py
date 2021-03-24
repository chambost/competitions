def can_fit(aa,ss,ee) :
  return not any( aa[x] for x in range(ss,ee))
    
def solve() :
  NN = int(input())
  answer = [""] *  NN
  impossible = False
  CC = [ False ] * (24*60)
  JJ = [ False ] * (24*60)
  schedules = [(0,0,0)] * NN
  for jj in range(NN) :
    SS, EE = map(int,input().split())
    schedules[jj] = (SS, EE, jj)
  for ss,ee,kk in sorted(schedules) :
    if can_fit(CC, ss, ee) :
        answer[kk] = "C"
        for x in range(ss,ee):
            CC[x] = True
    elif can_fit(JJ, ss, ee) :
        answer[kk] = "J"
        for x in range(ss,ee):
            JJ[x] = True
    else :
        impossible = True
  return "IMPOSSIBLE" if impossible else "".join(answer)

TT = int(input())
for ii in range(1,1+TT) :
  print("Case #{}: {}".format(ii, solve()))
