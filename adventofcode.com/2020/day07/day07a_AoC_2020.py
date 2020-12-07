puzzleinput = r"""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


import re
graph = dict()
for line in puzzleinput.splitlines() :\
    bags = re.findall(r"(?:(?:\d+ )?([a-z ]*?) bag)",line)
    if bags[1] != "s contain no other" :
        graph[bags[0]] = bags[1:]
    else :
        graph[bags[0]] = []
count = 0
def recursive_search(value):
    if "shiny gold" in value :
        return 1
    else :
        for v in value :
            if recursive_search(graph[v]) == 1 :
                return 1
    return 0

for key,value in graph.items() :
    count += recursive_search(value)
        
print(count)
