from collections import defaultdict
import math
import re


def parse_tile(raw_tile):
    raw_title, *raw_image = raw_tile.split("\n")

    title_str = re.match(r"Tile (\d+):", raw_title).group(1)
    grid = {}

    for y, row in enumerate(raw_image):
        for x, cell in enumerate(row):
            grid[x, y] = cell

    return int(title_str), (x, y), grid


def parse_input(input_):
    return [parse_tile(raw_tile) for raw_tile in input_.split("\n\n")]


class TileImage:
    def __init__(self, id, size, grid):
        self.id = id
        self.max_x, self.max_y = size
        self.size_x = self.max_x + 1
        self.size_y = self.max_y + 1
        self.grid = grid

    def get_col_coordinates(self, col):
        return ((col, y) for y in range(self.size_y))

    def get_row_coordinates(self, row):
        return ((x, row) for x in range(self.size_x))

    def get_col(self, col):
        return "".join(self.grid[coord] for coord in self.get_col_coordinates(col))

    def get_row(self, row):
        return "".join(self.grid[coord] for coord in self.get_row_coordinates(row))


def match_edges(tiles):
    edges = defaultdict(list)

    for tile in tiles.values():
        tile_edges = [
            tile.get_col(0),
            tile.get_col(tile.max_x),
            tile.get_row(0),
            tile.get_row(tile.max_y),
        ]

        for edge in tile_edges:
            rv_edge = "".join(reversed(edge))

            edge_key = rv_edge if len(edges[rv_edge]) else edge

            edges[edge_key].append(tile.id)

    return dict((k, v) for k, v in edges.items() if len(v))


def part1(data):
    tiles = {tile_data[0]: TileImage(*tile_data) for tile_data in data}

    # Expected number of total edges is `4 * n * n`.
    # Expected number of unmatched edges is `4 * n`, so `4 * 7 = 28`.
    matching_edges = match_edges(tiles)
    
    # We don't need to actually arrange the tiles (so far), we just need to find the corner tiles?
    uncommon_edges = defaultdict(int)
    for edge in matching_edges.values():
        if len(edge) == 1:
            uncommon_edges[edge[0]] += 1

    return math.prod(k for k, v in uncommon_edges.items() if v == 2)


def part2(entries):
    pass
