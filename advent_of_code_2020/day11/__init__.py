MAP_VALUES = {
    "L": False,
    "#": True,
    ".": None,
    False: "L",
    True: "#",
    None: ".",
}


def parse_input(input_):
    grid = {}

    for y, row in enumerate(input_.split("\n")):
        for x, cell in enumerate(row):
            grid[(x, y)] = MAP_VALUES[cell]


    return grid


class SeatLayout:
    def __init__(self, grid):
        self.grid = grid

        x, y = list(zip(*grid.keys()))
        self.max_x = max(x) + 1
        self.max_y = max(y) + 1

    def __str__(self):
        str_ = ""

        for y in range(self.max_y):
            row = "".join(MAP_VALUES[self.grid[x, y]] for x in range(self.max_x))
            str_  += "\n" + row

        return 0#str_.strip()

    def next_state(self, position):
        x, y = position
        current_occupied = self.grid[position]

        neighbors = {(i, j) for i in range(max(x - 1, 0), min(x + 2, self.max_x)) for j in range(max(y - 1, 0), min(y + 2, self.max_y))}
        neighbors.remove(position)  # Remove `i=0, j=0`.

        occupieds = sum(bool(self.grid[neighbor]) for neighbor in neighbors)

        if current_occupied is False and occupieds == 0:
            return True
        elif current_occupied is True and occupieds >= 4:
            return False
        else:
            return current_occupied

    def next_grid(self):
        next_grid = self.grid.copy()

        for position, value in next_grid.items():
            if value is not None:
                next_grid[position] = self.next_state(position)

        if next_grid == self.grid:
            raise StopIteration
        else:
            self.grid = next_grid

    def occupied_seats(self):
        return sum(bool(value) for value in self.grid.values())


class FarseeingSeatLayout(SeatLayout):
    DIRECTIONS = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1),
    )

    def get_visible_neighbor(self, position, direction):
        x, y = position
        i, j = direction

        while True:
            x += i
            y += j

            if not 0 <= x < self.max_x:
                return None
            elif not 0 <= y < self.max_y:
                return None
            elif self.grid[x, y] is not None:
                return self.grid[x, y]
            # else: pass

    def next_state(self, position):
        x, y = position
        current_occupied = self.grid[position]

        visible_neighbors = [self.get_visible_neighbor(position, direction) for direction in self.DIRECTIONS]

        occupieds = sum(bool(neighbor) for neighbor in visible_neighbors)

        if current_occupied is False and occupieds == 0:
            return True
        elif current_occupied is True and occupieds >= 5:
            return False
        else:
            return current_occupied


def part1(grid):
    seat_layout = SeatLayout(grid.copy())

    try:
        while True:
            seat_layout.next_grid()
    except StopIteration:
        return seat_layout.occupied_seats()


def part2(grid):
    seat_layout = FarseeingSeatLayout(grid.copy())

    try:
        while True:
            seat_layout.next_grid()
    except StopIteration:
        return seat_layout.occupied_seats()
