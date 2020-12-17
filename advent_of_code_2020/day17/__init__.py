from collections import defaultdict


MAP_VALUES = {
    "#": True,
    ".": False,
}


def parse_input(input_):
    grid = {}

    for y, row in enumerate(input_.split("\n")):
        for x, cell in enumerate(row):
            grid[(x, y, 0)] = MAP_VALUES[cell]

    return grid


class PocketDimension:
    def __init__(self, initial_state):
        self.actives = [coordinate for coordinate, state in initial_state.items() if state is True]

        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        next_state = defaultdict(bool)
        region_of_interest = self.get_region_of_interest()

        for coordinate in region_of_interest:
            next_state[coordinate] = self.get_next_state(coordinate)

        self.actives = [coordinate for coordinate, state in next_state.items() if state is True]
        self.i += 1

    def get_region_of_interest(self):
        # Assign initial mins and maxs to actual active cells, in case the region around (0, 0, 0) is inactive.
        min_x, min_y, min_z = self.actives[0]
        max_x, max_y, max_z = self.actives[0]

        for coordinate in self.actives:
            x, y, z = coordinate

            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x

            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

            if z < min_z:
                min_z = z
            if z > max_z:
                max_z = z

        return [
            (x, y, z)
            for x in range(min_x - 1, max_x + 2)
            for y in range(min_y - 1, max_y + 2)
            for z in range(min_z - 1, max_z + 2)
        ]

    def get_next_state(self, coordinate):
        is_active = coordinate in self.actives
        active_neighbors = sum(neighbor in self.actives for neighbor in self.get_neighbor_coordinates(coordinate))

        if is_active is True and active_neighbors in [2, 3]:
            return True
        elif is_active is False and active_neighbors == 3:
            return True

        return False

    @staticmethod
    def get_neighbor_coordinates(center):
        x, y, z = center

        # TODO: do this programmatically without appending to a *live* `list`.
        coordinates = [
            (x - 1, y - 1, z - 1),
            (x, y - 1, z - 1),
            (x + 1, y - 1, z - 1),
            (x - 1, y, z - 1),
            (x, y, z - 1),
            (x + 1, y, z - 1),
            (x - 1, y + 1, z - 1),
            (x, y + 1, z - 1),
            (x + 1, y + 1, z - 1),
            (x - 1, y - 1, z),
            (x, y - 1, z),
            (x + 1, y - 1, z),
            (x - 1, y, z),
            (x, y, z),
            (x + 1, y, z),
            (x - 1, y + 1, z),
            (x, y + 1, z),
            (x + 1, y + 1, z),
            (x - 1, y - 1, z + 1),
            (x, y - 1, z + 1),
            (x + 1, y - 1, z + 1),
            (x - 1, y, z + 1),
            (x, y, z + 1),
            (x + 1, y, z + 1),
            (x - 1, y + 1, z + 1),
            (x, y + 1, z + 1),
            (x + 1, y + 1, z + 1),
        ]

        assert len(coordinates) == 27
        coordinates.remove(center)

        return coordinates


def part1(grid):
    pocket = PocketDimension(grid)

    for i in range(6):
        next(pocket)

    return len(pocket.actives)


def part2(entries):
    pass
