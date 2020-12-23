puzzleinput = r"""0,3,6"""
#puzzleinput = r"""1,3,2"""
#puzzleinput = r"""2,1,3"""
#puzzleinput = r"""1,2,3"""
#puzzleinput = r"""2,3,1"""
#puzzleinput = r"""3,2,1"""
#puzzleinput = r"""3,1,2"""

numbers = [int(n) for n in puzzleinput.split(",")]
for n in range(2020) :
    if numbers[-1] not in numbers[:-1] :
        numbers.append(0)
    else :
        numbers.append(1 + list(reversed(numbers[:-1])).index(numbers[-1]))
print(numbers[2020-1])
