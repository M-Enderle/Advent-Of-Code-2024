puzzle = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

puzzle_matrix = [[0 if char == "." else -1 if char == "#" else 1 for char in row] for row in puzzle.strip().split("\n")]
print(puzzle_matrix)