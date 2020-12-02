puzzleinput = r"""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

count = 0
for num,ch,password in (l.split() for l in puzzleinput.splitlines()) :
    min,max = num.split("-")
    min = int(min)
    max = int(max)
    ch,_ = ch.split(":")
    if password[min-1] == ch and password[max-1] != ch :
        count += 1
    if password[min-1] != ch and password[max-1] == ch :
        count += 1
print(count)
