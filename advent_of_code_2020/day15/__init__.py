from collections import defaultdict


def parse_input(input_):
    return [int(i) for i in input_.split(",")]


class MemoryGame:
    def __init__(self, starting_numbers):
        self.starting_numbers = starting_numbers.copy()

        self.last_number = None
        self.past_numbers = defaultdict(int)
        self.current_turn = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_turn += 1

        if len(self.starting_numbers):
            number = self.starting_numbers.pop(0)
        else:
            last_spoken = self.past_numbers[self.last_number]

            number = self.current_turn - 1 - last_spoken if last_spoken else 0

        if self.last_number is not None:
            self.past_numbers[self.last_number] = self.current_turn - 1
        self.last_number = number


def part1(starting_numbers):
    game = MemoryGame(starting_numbers)

    for i in range(2020):
        next(game)

    return game.last_number


def part2(starting_numbers):
    attempts = 30_000_000
    game = MemoryGame(starting_numbers)

    for i in range(attempts):
        next(game)

    return game.last_number
