puzzleinput = r""""""

def solve_day01a_aoc_2015(puzzleinput) :
    return sum(       1 if c == "(" 
                else -1 if c == ")" 
                else  0 
                for c in puzzleinput 
              )
    
print(solve_day01a_aoc_2015( "(())" ))
print(solve_day01a_aoc_2015( "()()" ))

print(solve_day01a_aoc_2015( "(((" ))
print(solve_day01a_aoc_2015( "(()(()(" ))

print(solve_day01a_aoc_2015( "))(((((" ))

print(solve_day01a_aoc_2015( "())" ))
print(solve_day01a_aoc_2015( "))(" ))

print(solve_day01a_aoc_2015( ")))" ))
print(solve_day01a_aoc_2015( ")())())" ))

print(solve_day01a_aoc_2015( puzzleinput ))
