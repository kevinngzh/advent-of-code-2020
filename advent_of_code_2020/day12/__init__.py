def parse_input(input_):
    return [(instruction[0], int(instruction[1:])) for instruction in input_.split("\n")]


DIRECTIONS = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


class NavigationComputer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.index = 0

        self.direction = "E"
        self.x = 0
        self.y = 0

    def __iter__(self):
        return self

    def __next__(self):
        action, value = self.instructions[self.index]

        if action in "LR":
            self.turn(action, value)
        else:
            direction = self.direction if action == "F" else action

            self.forward(direction, value)

        self.index += 1

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def turn(self, direction, value):
        clockwise_turns = int(value / 90)
        direction_indices = list(DIRECTIONS.keys())

        if direction == "L":
            clockwise_turns *= -1

        new_direction_index = (direction_indices.index(self.direction) + clockwise_turns) % 4

        self.direction = direction_indices[new_direction_index]

    def forward(self, direction, value):
        base_x, base_y = DIRECTIONS[direction]
        move_x = base_x * value
        move_y = base_y * value

        self.x += move_x
        self.y += move_y


def part1(instructions):
    nav = NavigationComputer(instructions)

    while True:
        try:
            next(nav)
        except IndexError:
            return nav.manhattan_distance


def part2(entries):
    pass
