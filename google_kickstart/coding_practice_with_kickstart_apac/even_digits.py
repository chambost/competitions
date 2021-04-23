TT = int(input())
for t in range(1,1+TT) :
    NN = int(input())
    upsteps,downsteps = 0,0
    first = False
    downfirst = False
    for i,c in enumerate(str(NN)) :
        if c == "1" and len(str(NN)) == 1 and not downfirst :
            downfirst = True
            downsteps = 1
        if c == "1" and len(str(NN)) != 1 and not downfirst :
            downfirst = True
            number = ""
            for j in range(i,len(str(NN))) :
                number += str(NN)[j]
            downsteps = int(number)-int("8" * (len(str(NN))-i-1))
        if c in ("3","5","7","9") and not downfirst :
            downfirst = True
            number = ""
            for j in range(i,len(str(NN))) :
                number += str(NN)[j]
            downsteps = int(number)-int(str(int(c)-1) + ("8" * (len(str(NN))-i-1)))
        if c == "9" and i == 0 and not first :
            first = True
            upsteps = int("20" + ("0" * (len(str(NN))-1)))-NN
        if c == "9" and not first :
            first = True
            number = ""
            for j in range(i,len(str(NN))) :
                number += str(NN)[j]
            upsteps = int("20" + ("0" * (len(str(NN))-i-1)))-int(number)
        if c in ("1","3","5","7") and not first :
            first = True
            number = ""
            for j in range(i,len(str(NN))) :
                number += str(NN)[j]
            upsteps = int(str(int(c)+1) + ("0" * (len(str(NN))-i-1)))-int(number)
    print(f"Case #{t}: {min(downsteps,upsteps)}")
            
