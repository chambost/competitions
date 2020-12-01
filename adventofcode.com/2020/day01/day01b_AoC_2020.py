inp = """
"""

numbers = set(int(x) for x in inp.split())
for n in numbers :
  for m in numbers - { n } :
    if 2020 - n - m in numbers :
        print(n * m * (2020-n-m))
