from collections import namedtuple
import re


SEAT_PATTERN = re.compile(r"([BF]{7})([LR]{3})")
Seat = namedtuple("Seat", ["boarding_pass", "row", "column", "seat_id"])


def parse_input(input_):
    return input_.split("\n")


def binary_search_str(str_, halves):
    search_space = list(range(2 ** len(str_)))

    for char in str_:
        half = int(len(search_space) / 2)

        if char == halves[0]:
            search_space = search_space[:half]
        elif char == halves[1]:
            search_space = search_space[half:]
        else:
            raise ValueError

    assert len(search_space) == 1

    return search_space[0]


def generate_seat_id(boarding_pass):
    row_str, column_str = SEAT_PATTERN.match(boarding_pass).groups()

    row = binary_search_str(row_str, ("F", "B"))
    column = binary_search_str(column_str, ("L", "R"))

    return Seat(boarding_pass, row, column, (row * 8) + column)


def part1(entries):
    pass


def part2(entries):
    pass
