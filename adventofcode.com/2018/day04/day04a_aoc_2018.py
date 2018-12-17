from datetime import datetime

log = []

try :
  while True :
    timestamp,message = raw_input().split("]")
    timestamp = datetime.strptime( timestamp.strip("[") , "%Y-%m-%d %H:%M" )
    log.append([timestamp,message])

except EOFError :
  pass

log = sorted( log )

guards = dict()

guardid = 0
minute = 0

for entry in log :
  if "#" in entry[1] :
    guardid = int( entry[1].split()[1].strip("#") )
    if guardid not in guards :
      guards[guardid] = [ 0 ] * 60
  elif "falls" in entry[1] :
    minute = entry[0].minute
  elif "wakes" in entry[1] :
    for ii in range(minute, entry[0].minute) :
      guards[guardid][ii] += 1

from pprint import pprint

def sleepiest_id() :
  data = [ (sum(mm),id) for id,mm in guards.iteritems() ]
  data = sorted( data )
  return data[-1][1]

sid = sleepiest_id()
minute = guards[sid].index( max( guards[sid] ))

print sid * minute
