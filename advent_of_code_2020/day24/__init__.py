from collections import defaultdict


HEX_DIRECTIONS = {
    "nw": (0, -1),
    "ne": (1, -1),
    "w": (-1, 0),
    "e": (1, 0),
    "sw": (-1, 1),
    "se": (0, 1),
}


def parse_tiles(raw_tiles):
    i = 0
    tiles = []

    while i < len(raw_tiles):
        direction = ""

        if (char := raw_tiles[i]) in "ns":
            direction += char
            i += 1

        direction += raw_tiles[i]

        tiles.append(direction)
        i += 1

    return tiles


def parse_input(input_):
    return [parse_tiles(raw_tiles) for raw_tiles in input_.split("\n")]


def get_tile_coordinates(tile_directions):
    x = 0
    y = 0

    for direction in tile_directions:
        i, j = HEX_DIRECTIONS[direction]

        x += i
        y += j

    # `x`, `y` at the end of the `for` loop is the tile we're interested in.
    return x, y


def part1(tile_directions):
    tiles = defaultdict(int)

    for directions in tile_directions:
        coordinates = get_tile_coordinates(directions)
        tiles[coordinates] += 1

    # Tiles start as white, then gets flipped to black, then back to white, so if a tile gets flipped an odd number of times it's black.
    return sum(flipped_times % 2 == 1 for flipped_times in tiles.values())


def part2(entries):
    pass
