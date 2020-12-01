puzzleinput = r"""1212"""
#puzzleinput = r"""1221"""
#puzzleinput = r"""123425"""
#puzzleinput = r"""123123"""
#puzzleinput = r"""12131415"""

half = len(puzzleinput)//2
print(sum(int(a) for a,b in ((puzzleinput[x],puzzleinput[x+half]) for x in range(-half,len(puzzleinput)-half)) if a==b))
