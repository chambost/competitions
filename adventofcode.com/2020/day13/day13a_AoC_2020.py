puzzleinput = r"""939
7,13,x,x,59,x,31,19"""

busids = []
start,buses = puzzleinput.splitlines()
for bus in buses.split(",") :
    if bus == "x" :
        continue
    bus = int(bus)
    busids.append(bus)
start = int(start)
def solve() :
    curr = start
    while True:
        for id in busids :
            if curr % id == 0 :
                return id * (curr - start)
        curr += 1
print(solve())
