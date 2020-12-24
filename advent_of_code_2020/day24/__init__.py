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


def get_tile_state(tile_directions):
    tiles = defaultdict(bool)

    for directions in tile_directions:
        coordinates = get_tile_coordinates(directions)
        tiles[coordinates] = not tiles[coordinates]

    return tiles


def part1(tile_directions):
    tiles = get_tile_state(tile_directions)

    # Tiles start as white, then gets flipped to black, then back to white, so if a tile gets flipped an odd number of times it's black.
    return sum(tiles.values())


def get_next_state(tiles):
    next_state = defaultdict(bool)
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    for x, y in tiles:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    for x in range(min_x - 2, max_x + 3):
        for y in range(min_y - 2, max_y + 3):
            blacks = 0

            for i, j in HEX_DIRECTIONS.values():
                p = x + i
                q = y + j

                blacks += tiles[p, q]

            if tiles[x, y]:
                if blacks in [1, 2]:
                    next_state[x, y] = True
            else:
                if blacks == 2:
                    next_state[x, y] = True

    return next_state


def part2(tile_directions):
    tiles = get_tile_state(tile_directions)
    
    for i in range(100):
        tiles = get_next_state(tiles)

    return sum(tiles.values())
