puzzleinput = r"""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

grid = puzzleinput.splitlines()

product = 1
for dx,dy in ((1,1),(3,1),(5,1),(7,1),(1,2)) :
    count = 0
    width = len(grid[0])
    x = 0
    y = 0
    while y < len(grid) :
        if grid[y][x] == "#" :
            count += 1
        x = (x+dx) % width
        y += dy
    product *= count
print(product)
