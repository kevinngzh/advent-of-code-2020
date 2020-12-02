from collections import namedtuple
import re


PATTERN = re.compile(r"(\d+)-(\d+) (\w+): (\w+)")

Policy = namedtuple("Policy", ["min", "max", "letter"])


def parse_line(line):
    match = PATTERN.match(line)

    min_, max_, letter, password = match.groups()

    return Policy(int(min_), int(max_), letter), password


def parse_input(input_):
    return list(map(parse_line, input_.split("\n")))


def is_valid_password(entry):
    policy, password = entry
    letter_count = 0

    for letter in password:
        if letter == policy.letter:
            letter_count += 1

    return policy.min <= letter_count <= policy.max


def part1(entries):
    return sum(map(is_valid_password, entries))


def part2(entries):
    pass
