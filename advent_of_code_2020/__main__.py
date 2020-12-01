__version__ = '0.1.1'


import sys


raw_example = """
1721
979
366
299
675
1456
"""

example = [int(i) for i in raw_example.strip().split("\n")]


def part1(entries):
    pairs = set()

    for i in entries:
        for j in entries:
            if i + j == 2020:
                pairs.add((i, j))

    return {frozenset((i, j)): i * j for i, j in pairs}


def part2(entries):
    trips = set()

    for i in entries:
        for j in entries:
            for k in entries:
                if i + j + k == 2020:
                    trips.add((i, j, k))

    return {frozenset((i, j, k)): i * j * k for i, j, k in trips}


if __name__ == "__main__":
    if len(args := sys.argv[1:]) > 0:
        filepath = sys.argv[1]

        with open(filepath) as f:
            entries = [int(i) for i in f.readlines()]
    else:
        entries = example

    print(part1(entries))
    print(part2(entries))
