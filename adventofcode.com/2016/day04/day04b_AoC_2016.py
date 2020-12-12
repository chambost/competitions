puzzleinput = r""""""

from collections import Counter

import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

for line in puzzleinput.splitlines() :
    room,remainder = line.rsplit("-",1)
    sector,remainder = remainder.split("[")
    sector = int(sector)
    checksum = remainder[:-1]
    letters = Counter(room)
    del letters["-"]
    sl = sorted(letters.most_common(),key=lambda pair: pair[0])
    sl = sorted(sl,key=lambda pair: pair[1],reverse=True)
    if "".join(pair[0] for pair in sl[:5]) == checksum :
        if caesar(room,sector%26) == "northpole-object-storage" :
            print(sector)
