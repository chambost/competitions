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

count = 0
width = len(grid[0])
x = 0
y = 0
while y < len(grid) :
    if grid[y][x] == "#" :
        count += 1
    x = (x+3) % width
    y += 1
print(count)
