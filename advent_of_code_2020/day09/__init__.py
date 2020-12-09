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


def part2(data):
    first_invalid = part1(data)

    for first in range(len(data)):
        for last in range(first + 1, len(data)):
            print(first, last)

            contiguous_sum = sum(data[first:last])

            if contiguous_sum == first_invalid:
                min_, *_, max_ = sorted(data[first:last])

                return min_ + max_
            elif contiguous_sum > first_invalid:
                break
