puzzleinput = r"""1122"""
#puzzleinput = r"""1111"""
#puzzleinput = r"""1234"""
#puzzleinput = r"""91212129"""

print(sum(int(a) for a,b in ((puzzleinput[x],puzzleinput[x+1]) for x in range(-1,len(puzzleinput)-1)) if a==b))
