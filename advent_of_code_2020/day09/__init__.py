def parse_input(input_):
    return [int(num) for num in input_.split("\n")]


def is_valid(preamble, number):
    for preamble_num in preamble:
        if number - preamble_num in preamble:
            return True

    return False


def part1(data, preamble_length=25):
    for i in range(preamble_length, len(data)):
        if not is_valid(data[i-preamble_length : i], data[i]):
            return data[i]


def part2(entries):
    pass
