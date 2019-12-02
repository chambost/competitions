puzzleinput = r""""""

from itertools import accumulate
from itertools import dropwhile

numerise = lambda x : 1 if x == '(' else -1
solve2 = lambda x : next(dropwhile( lambda x : x[1] is not -1
                                  , enumerate( accumulate(numerise(c) for c in x)
                                             , start=1
                                             )
                        ))[0]
print(solve2(puzzleinput))
