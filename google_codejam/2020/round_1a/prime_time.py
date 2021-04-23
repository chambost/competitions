from collections import Counter
from itertools import combinations
from functools import reduce
from operator import mul

def score(first,second) :
    tally = sum(first)
    if tally == reduce(mul,second.elements(),1) :
        return tally
    return 0

TT = int(input())
for t in range(1,1+TT) :
    MM = int(input())
    primes = Counter()
    for m in range(MM) :
        PP, NN = (int(x) for x in input().split())
        primes[PP] = NN
    top = 0 
    for i in range(1,sum(primes.values())) :
        for first in combinations(primes.elements(),i) :
            second = primes - Counter(first)
            top = max(top,score(first,second))
    print(f"Case #{t}: {top}")
