def parse_input(input_):
    return [int(i) for i in input_]


class CupGame:
    def __init__(self, cups):
        self.cups = cups

        self.move = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.move += 1

        current_cup, removed_cups, potential_destinations = self.get_move_cups()
        destination_cup = current_cup

        i=0
        while destination_cup not in potential_destinations:
            destination_cup -= 1

            if destination_cup < min(self.cups):
                destination_cup = max(self.cups)
            i+=1
            if i>100:
                raise RecursionError

        destination_idx = potential_destinations.index(destination_cup)

        self.cups = (
            potential_destinations[:destination_idx+1]
            + removed_cups
            + potential_destinations[destination_idx+1:]
            + [current_cup]
        )

    def get_move_cups(self):
        return self.cups[0], self.cups[1:4], self.cups[4:]

    def get_labels(self, from_=1):
        start_idx = self.cups.index(from_) + 1  # Start from the cup next to `1`.
        labels = []

        for i in range(len(self.cups) - 1):
            idx = (start_idx + i) % len(self.cups)
            labels.append(str(self.cups[idx]))

        return int("".join(labels))


def part1(cups):
    game = CupGame(cups)

    for i in range(100):
        next(game)

    return game.get_labels()


def part2(entries):
    pass
