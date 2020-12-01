"""
Advent of Code 2020 solutions.

Usage:
    advent_of_code_2020 <input_file>
    advent_of_code_2020 -h | --help
    advent_of_code_2020 --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""


__version__ = "0.1.3"


import sys

from docopt import docopt
from schema import Schema, Use


if __name__ == "__main__":
    from day01 import example, part1, part2

    s = Schema({
        "<input_file>": Use(open),
    }, ignore_extra_keys=True)

    args = s.validate(docopt(__doc__, version=__version__))

    entries = [int(i) for i in args["<input_file>"].readlines()]

    print(part1(entries))
    print(part2(entries))
