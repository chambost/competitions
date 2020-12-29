puzzleinput = r"""0,3,6"""
#puzzleinput = r"""1,3,2"""
#puzzleinput = r"""2,1,3"""
#puzzleinput = r"""1,2,3"""
#puzzleinput = r"""2,3,1"""
#puzzleinput = r"""3,2,1"""
#puzzleinput = r"""3,1,2"""

target = 30000000
numbers = [int(n) for n in puzzleinput.split(",")]
past_indices = defaultdict(list)
for i,n in enumerate(numbers) :
    past_indices[n].append(i)
for i in range(len(numbers), target) :
    last = numbers.pop()
    if len(past_indices[last]) == 1 :
        numbers.append(last)
        numbers.append(0)
        past_indices[0].append(i)
    else :
        next = past_indices[last][-1] - past_indices[last][-2]
        numbers.append(last)
        numbers.append(next)
        past_indices[next].append(i)
print(numbers[target-1])
