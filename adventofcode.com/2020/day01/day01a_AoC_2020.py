inp = """
"""

numbers = [int(x) for x in inp.split()]
for n in numbers :
  if 2020 - n in numbers :
    print(n * (2020-n))
