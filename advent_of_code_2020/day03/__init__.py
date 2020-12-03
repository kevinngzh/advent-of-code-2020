import math


MAP_VALUES = {
    "#": True,
    ".": False,
}


def parse_input(input_):
    grid = {}

    for y, row in enumerate(input_.split("\n")):
        for x, cell in enumerate(row):
            grid[(x, y)] = MAP_VALUES[cell]

    return grid


def get_trees_encountered(grid, slope):
    # Start at the top-left corner.
    current_pos = [0, 0]
    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    trees_count = 0

    while current_pos[1] <= (max_y - 1):
        current_pos = (current_pos[0] + slope[0]) % (max_x + 1), current_pos[1] + slope[1]

        trees_count += grid[current_pos]

    return trees_count


def part1(grid):
    return get_trees_encountered(grid, (3, 1))


def part2(grid):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    slope_trees = [get_trees_encountered(grid, slope) for slope in slopes]

    return math.prod(slope_trees)
