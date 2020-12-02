def parse_input(input_):
    return [int(i) for i in input_.split("\n")]


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
