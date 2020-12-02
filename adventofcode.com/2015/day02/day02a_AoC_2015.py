puzzleinput = r"""2x3x4"""
#puzzleinput = r"""1x1x10"""

area = 0
for l,w,h in (line.split("x") for line in puzzleinput.splitlines()) :
    l = int(l)
    w = int(w)
    h = int(h)
    area += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
print(area)
