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


def part2(joltages):
    sorted_joltages = sorted(joltages)

    # Since the built-in adapter is always 3 higher than then highest adapter, the highest adapter must ALWAYS be part of an arrangement.
    # Not necessary true of the lowest adapter; if both 1 jolt and 3 jolt adapters are present, we can select either of them.

    found_ways = {0: 1}

    for joltage in sorted_joltages:
        joltage_way = 0

        for difference in range(1, 4):
            joltage_difference = joltage - difference

            if joltage_difference in found_ways:
                joltage_way += found_ways[joltage_difference]

        found_ways[joltage] = joltage_way

    return found_ways[max(joltages)]

