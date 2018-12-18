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

from pprint import pprint

times = { 'A':61 
        , 'B':62
        , 'C':63
        , 'D':64
        , 'E':65
        , 'F':66
        , 'G':67
        , 'H':68
        , 'I':69
        , 'J':70
        , 'K':71
        , 'L':72
        , 'M':73
        , 'N':74
        , 'O':75
        , 'P':76
        , 'Q':77
        , 'R':78
        , 'S':79
        , 'T':80
        , 'U':81
        , 'V':82
        , 'W':83
        , 'X':84
        , 'Y':85
        , 'Z':86
}

avail = list( aas - bbs )
avail.sort(reverse=True)
answer = []
complete = []
elves = [ [0,0,0,0,0] , ["." , "." , "." , "." , "." ] ]
time = 0
while len(avail) != 0 or sum(elves[0]) != 0 :
  for ii in range(len(elves[0])) :
    if elves[0][ii] == 0 and len(avail) > 0 :
      next = avail.pop()
      answer.append(next)
      elves[0][ii] = times[next]
      elves[1][ii] = next
  step = min(set(elves[0]) - set([0]))
  for ii in range(len(elves[0])) :
    if elves[0][ii] == step :
      complete.append( elves[1][ii] )
  for ii in range(len(elves[0])) :
    if elves[0][ii] == step :
      if adj.has_key(elves[1][ii]) :
        for node in adj[elves[1][ii]] :
          if set(radj[node]).issubset(complete) :
            avail.append( node )
            avail = set(avail)
            avail -= set(complete)
            avail -= set(answer)
            avail = list(avail)
            avail.sort(reverse=True)

  time += step
  elves[0][0] -= step if elves[0][0] != 0 else 0
  elves[0][1] -= step if elves[0][1] != 0 else 0
  elves[0][2] -= step if elves[0][2] != 0 else 0
  elves[0][3] -= step if elves[0][3] != 0 else 0
  elves[0][4] -= step if elves[0][4] != 0 else 0

print time
