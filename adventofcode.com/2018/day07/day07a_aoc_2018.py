adj = dict()
radj = dict()
aas = set()
bbs = set()

try :
  while True :
    _,a,_,_,_,_,_,b,_,_ = raw_input().split()
    if not adj.has_key(a) :
      adj[a] = []
    if not radj.has_key(b) :
      radj[b] = []
    adj[a].append(b)
    radj[b].append(a)
    aas.add(a)
    bbs.add(b)
except EOFError :
  pass

avail = list( aas - bbs )
avail.sort(reverse=True)
answer = []
while len(avail) != 0 :
  next = avail.pop()
  answer.append(next)
  if adj.has_key(next) :
    for node in adj[next] :
      if set(radj[node]).issubset(answer) :
        avail.append( node )
  avail = set(avail)
  avail -= set(answer)
  avail = list(avail)
  avail.sort(reverse=True)

print "".join( answer ) 
  
