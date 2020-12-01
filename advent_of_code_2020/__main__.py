__version__ = "0.1.2"


import sys


if __name__ == "__main__":
    from day01 import example, part1, part2

    if len(args := sys.argv[1:]) > 0:
        filepath = sys.argv[1]

        with open(filepath) as f:
            entries = [int(i) for i in f.readlines()]
    else:
        entries = example

    print(part1(entries))
    print(part2(entries))
