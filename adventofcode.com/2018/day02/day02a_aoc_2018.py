from collections import Counter
  
twos = 0
threes = 0
try :
  while True :
    bag = Counter(raw_input()).values()
    twos += 1 if 2 in bag else 0
    threes += 1 if 3 in bag else 0
except EOFError :
  pass
print twos * threes
