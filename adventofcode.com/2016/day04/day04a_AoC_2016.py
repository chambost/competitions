puzzleinput = r"""aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""

from collections import Counter

count = 0
for line in puzzleinput.splitlines() :
    letters,remainder = line.rsplit("-",1)
    sector,remainder = remainder.split("[")
    sector = int(sector)
    checksum = remainder[:-1]
    letters = Counter(letters)
    del letters["-"]
    sl = sorted(letters.most_common(),key=lambda pair: pair[0])
    sl = sorted(sl,key=lambda pair: pair[1],reverse=True)
    if "".join(pair[0] for pair in sl[:5]) == checksum :
        count += sector
print(count)
