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


def part1(boarding_passes):
    seat_ids = [generate_seat_id(boarding_pass).seat_id for boarding_pass in boarding_passes]

    return max(seat_ids)


def part2(boarding_passes):
    seat_ids = sorted(generate_seat_id(boarding_pass).seat_id for boarding_pass in boarding_passes)

    results = []

    # Iterate from second `seat_id` to the second-last `seat_id`.
    # We are interested in `seat_id`s where `seat_id + 1` or `seat_id - 1` is
    # not in `seat_ids`.
    # Actual result should be between the two items in `results`?
    for seat_id in seat_ids[1:-1]:
        if seat_id + 1 not in seat_ids or seat_id - 1 not in seat_ids:
            results.append(seat_id)

    return results
