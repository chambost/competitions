puzzleinput = r"""2x3x4"""
#puzzleinput = r"""1x1x10"""

ribbon = 0
for l,w,h in (line.split("x") for line in puzzleinput.splitlines()) :
    l = int(l)
    w = int(w)
    h = int(h)
    ribbon += 2*min(l+w,w+h,h+l) + l*w*h
print(ribbon)
