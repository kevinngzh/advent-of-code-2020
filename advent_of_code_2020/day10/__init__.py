def parse_input(input_):
    return [int(num) for num in input_.split("\n")]


def part1(joltages):
    sorted_joltages = sorted(joltages)
    current_joltage = 0
    differences = [0, 0, 1]  # Built-in adapter is always 3 higher than highest adapter.

    for joltage in sorted_joltages:
        difference = joltage - current_joltage

        current_joltage = joltage
        differences[difference - 1] += 1

    return differences[0] * differences[2]


def part2(entries):
    pass
