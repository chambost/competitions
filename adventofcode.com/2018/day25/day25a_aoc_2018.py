puzzleinput = r""""""

testinput0 = r"""0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0"""

testinput1 = r"""-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0"""

testinput2 = r"""1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2"""

testinput3 = r"""1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2"""

def distance(a,b) :
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])+abs(a[3]-b[3])

def solve_day25a_aoc_2018(choseninput) :
    points = []
    for line in choseninput.split("\n") :
        t,z,y,x = [int(_) for _ in line.split(",")]
        points.append((t,z,y,x))
        
    ll = len(points)
    matrix = [[0 for _ in range(ll)] for _ in range(ll)]
    for ii in range(ll) :
        for jj in range(ii) :
            d = distance(points[ii],points[jj])
            matrix[jj][ii] = d
            matrix[ii][jj] = d
    constellations = [0] * ll
    label = 0
    while any((x==0 for x in constellations)) :
        label += 1
        def tag(jj) :
            constellations[jj] = label
            for kk,distance in enumerate(matrix[jj]) :
                if distance <= 3 and constellations[kk] == 0 :
                    tag(kk)
        for ii in range(ll) :
            if constellations[ii] == 0 :
                tag(ii)
                break
    return label
    
solve_day25a_aoc_2018(testinput0)
solve_day25a_aoc_2018(testinput1)
solve_day25a_aoc_2018(testinput2)
solve_day25a_aoc_2018(testinput3)
