def solve_day23b_aoc_2018(choseninput) :

    nanobot_input = choseninput.split("\n")
    nanobots = []
    
    index = 0
    for nanobot in nanobot_input :
        first,second = nanobot.split(", ")
        x,y,z = ( int(_) for _ in first.strip("pos=<").strip(">").split(",") )
        r = int( second.strip("r="))
        if (x,y,z) == (104938337,44789181,4144431) or (x,y,z) == (36865619,54614560,46191179) :
            print(index,r,z,y,x)
        nanobots.append((r,z,y,x))
        index += 1

    def does_overlap(first,second) :
        return abs(first[1]-second[1])+abs(first[2]-second[2])+abs(first[3]-second[3]) <= first[0]+second[0]


        
    print(sum((does_overlap(nanobots[64],nb) for nb in nanobots)))
    print(sum((does_overlap(nanobots[724],nb) for nb in nanobots )))
# # #     def overlap(first,second) :
# # #         return abs(first[1]-second[1])+abs(first[2]-second[2])+abs(first[3]-second[3]) <= first[0]+second[0]

        
    
    def count(z,y,x) :
        count = 0
        for nanobot in nanobots :
            count += 1 if abs(nanobot[1]-z)+abs(nanobot[2]-y)+abs(nanobot[3]-x) <= nanobot[0] else 0    
        return count
    
    def dist(z,y,x) :
        return (abs(x-104938337)+abs(y-44789181)+abs(z-4144431)-70340192
               ,abs(x-36865619)+abs(y-54614560)+abs(z-46191179)-49604656
               )
    
    def findanswer(z,y,x) :
        cc = count(z,y,x)
#         if cc > 889 :
        print(cc,z+y+x,z,y,x,dist(z,y,x))
        
    def searchanswer(z,y,x,d) :
        findanswer(z, y, x)
        findanswer(z+d, y, x)
        findanswer(z, y+d, x)
        findanswer(z, y, x+d)

    def strafeanswer_y(z,y,x,d) :
        size = 10000
        for nn in range(d//size) :
#             print("yy",nn)
            findanswer(z+nn*size,y-nn*size,x)
            strafeanswer_x(z+nn*size,y-nn*size,x,
                         min(54614560-(y-nn*size)
                            ,104938337-x))
            
    def strafeanswer_x(z,y,x,d) :
        size = 10000
        for nn in range(d//size) :
#             print("xx",nn)
            findanswer(z,y+nn*size,x+nn*size)
    
    def increaseanswer(z,y,x,vv,dd) :
        print("a")
        findanswer( z , y , x )
        cc = 0
        while True: 
            print("b")
            cc += dd
            if count(z,y+cc,x+cc) == vv :
                findanswer( z , y+cc , x+cc )
            else :
                break
        print("c")
        cc = 0
        while True: 
            cc += dd
            if count(z,y-cc,x-cc) == vv :                
                findanswer( z , y-cc , x-cc ) 
            else :
                break
        cc = 0
        while True: 
            cc += dd
            if count(z+cc,y-cc,x) == vv :        
                findanswer( z+cc , y-cc , x )
            else :
                break
        cc = 0
        while True: 
            cc += dd
            if count(z-cc,y+cc,x) == vv :                  
                findanswer( z-cc , y+cc , x )
            else :
                break
        cc = 0
        while True: 
            cc += dd
            if count(z+cc,y,x+cc) == vv :   
                findanswer( z+cc , y , x+cc )
            else :
                break
        cc = 0
        while True: 
            cc += dd
            if count(z-cc,y,x-cc) == vv :  
                findanswer( z-cc , y , x-cc )
            else :
                break
        
        print("d")
                
    def shiftanswer(z,y,x) :
        findanswer( z , y+1 , x )
        findanswer( z , y+2 , x )
        findanswer( z , y+3 , x )        
#         findanswer( z , y , x+1 )
#         findanswer( z , y , x+2 )
#         findanswer( z , y , x+3 ) 
        
#         findanswer( z , y-1 , x ) 
#         findanswer( z , y-2 , x ) 
#         findanswer( z , y-3 , x ) 
        findanswer( z , y , x-1 ) 
        findanswer( z , y , x-2 ) 
        findanswer( z , y , x-3 ) 
        
        findanswer( z+1 , y , x )
        findanswer( z+2 , y , x )
        findanswer( z+3 , y , x )
#         findanswer( z , y-1 , x )
#         findanswer( z , y-2 , x )
#         findanswer( z , y-3 , x )

#         findanswer( z-1 , y , x )
#         findanswer( z-2 , y , x )
#         findanswer( z-3 , y , x )
#         findanswer( z , y+1 , x )
#         findanswer( z , y+2 , x )
#         findanswer( z , y+3 , x )
            
#         findanswer( z+1 , y , x )
#         findanswer( z+2 , y , x )
#         findanswer( z+3 , y , x )
# #         findanswer( z , y , x+1 )
# #         findanswer( z , y , x+2 )
# #         findanswer( z , y , x+3 )

    
# #         findanswer( z-1 , y , x )
# #         findanswer( z-2 , y , x )
# #         findanswer( z-3 , y , x )
#         findanswer( z , y , x-1 )
#         findanswer( z , y , x-2 )
#         findanswer( z , y , x-3 )





    increaseanswer( 13209446, 46554241, 45428220, 976, 1 )


#     shiftanswer( 13209446, 46554241, 45428220) #, 976, 1 )
#     shiftanswer( 13209446, 46554240, 45428222) #, 964, 1 )
        
#     findanswer( 14844431 , 46556652+10 , 47065619+10 )
#     findanswer( 14844431+10 , 46556652-10 , 47065619 )
#     findanswer( 14844431+10 , 46556652 , 47065619+10 )
    return



#976 105191907 13209446 46554241 45428220 (0, -3)
# 973 105191911 13209446 46554243 45428222 (0, -3)

#964 105191908 13209446 46554240 45428222 (-3, 0)

#963 105191912 13209448 46554240 45428224 (-3, 0)

#962 105191918 13209451 46554240 45428227 (-3, 0)

#961 105191920 13209452 46554240 45428228 (-3, 0)
#961 105191922 13209451 46554242 45428229 (-3, 0)

#960 105191926 13209455 46554240 45428231 (-3, 0)
#960 105191930 13209457 46554240 45428233 (-3, 0)
#960 105191924 13209452 46554242 45428230 (-3, 0)
    increaseanswer( 13209458, 46554242, 45428236, 957, 1 )


    increaseanswer( 13209461 ,46554242 ,45428239, 956, 1 )


    increaseanswer( 13209451 ,46554252, 45428239, 949, 5 )


    increaseanswer( 13209481 ,46554252, 45428269, 939, 30 )


    increaseanswer( 13209531 ,46554252, 45428319, 926, 50 )


    increaseanswer( 13209531 ,46554352 ,45428419, 905, 100 )


    increaseanswer( 13209631, 46556652, 45430819, 897, 100 )

    increaseanswer( 13344431 ,46556652 ,45565619, 894, 100 )
    increaseanswer( 13844431 , 46556652 , 46065619 , 500000 )

    increaseanswer( 14844431 , 46556652 , 47065619 , 1000000 )


#     strafeanswer_y( 14844431 , 46556652 , 47065619 , 46556652-44789181 )
    
            
# 889 108466702 14844431 46556652 47065619 (-3, 0)
            
    findanswer( 6244431 , 54456652 , 46365619 )
    strafeanswer_y( 6244431 , 54456652 , 46365619, 54456652-44789181)
    
    print()
    print(" ~ ~ ~")
    print()
    
#     64 70340192 4144431 44789181 104938337
# 724 49604656 46191179 54614560 36865619
# 980
# 976
# 635 107066702 6244431 54456652 46365619 (-3, 0)
        
    searchanswer(4144431, 44789181, 36865619, 0)    
    searchanswer(4144431, 44789181, 36865619, 2267471)
    searchanswer(4144431, 44789181, 36865619, 2267474)

    strafeanswer_y(4144431, 44789181+2267471, 36865619, 2267471)

    
    
    return
    counts = []
    for nanobot in nanobots :
        counts.append( count(nanobot[1],nanobot[2],nanobot[3]))
        
    print(counts)
        
    ll = len(nanobots)
    
    start = (21533377,48852586,76786034)

    def region(z,y,x) :
        print(count(*start))
        print(count(z+1,y,x))
        print(count(z-1,y,x))
        print(count(z,y+1,x))
        print(count(z,y-1,x))
        print(count(z,y,x+1))
        print(count(z,y,x-1))
        
    region(*start)
    region(21533377+10000000,48852586,76786034)
    region(21533377-10000000,48852586,76786034)
    region(21533377,48852586+10000000,76786034)
    region(21533377,48852586-10000000,76786034)
    region(21533377,48852586,76786034+10000000)
    region(21533377,48852586,76786034-10000000)

solve_day23b_aoc_2018(puzzleinput)
