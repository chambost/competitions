puzzleinput = r"""939
7,13,x,x,59,x,31,19"""

#puzzleinput = r"""939
#17,x,13,19"""

#puzzleinput = r"""939
#67,7,59,61"""

#puzzleinput = r"""939
#67,x,7,59,61"""

#puzzleinput = r"""939
#67,7,x,59,61"""

#puzzleinput = r"""939
#1789,37,47,1889"""


from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

start,buses = puzzleinput.splitlines()
print(chinese_remainder(*zip(*((int(id),-n) for n,id in enumerate(buses.split(",")) if id != "x"))))

    
