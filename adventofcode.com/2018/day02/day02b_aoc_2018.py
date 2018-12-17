from collections import Counter
  
ss = []

try :
  while True :
    ss.append(raw_input())
except EOFError :
  pass

for ii in range(50) :
  ll = [ list(s) for s in ss ]
  for l in ll :
    del l[ii]
  bag = Counter(["".join(l) for l in ll])
  top = bag.most_common(1)[0]
  if top[1] == 2 :
    print top[0]
    exit()
