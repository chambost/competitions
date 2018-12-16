ll = []
try :
  while True :
    ll.append( int(input()) )
except EOFError :
  pass

ss = 0
memo = dict()
memo[0] = True
while True :
  for xx in ll :
    ss += xx
    if ss in memo :
      print ss
      exit()
    memo[ss] = True
print "No duplicate"
