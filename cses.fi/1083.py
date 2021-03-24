n = int(input())
nums = set(int(x) for x in input().split())
all_nums = set()
for i in range(1,1+n) :
    all_nums.add(i)
print((all_nums - nums).pop())

