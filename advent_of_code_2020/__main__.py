"""
Advent of Code 2020 solutions.

Usage:
    advent_of_code_2020 day <day> <input_file>
    advent_of_code_2020 -h | --help
    advent_of_code_2020 --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""


__version__ = "0.1.4"


import sys

from docopt import docopt
from schema import Schema, Use


if __name__ == "__main__":
    import importlib

    s = Schema({
        "<day>": Use(int),
        "<input_file>": Use(open),
    }, ignore_extra_keys=True)

    args = s.validate(docopt(__doc__, version=__version__))

    entries = [int(i) for i in args["<input_file>"].readlines()]

    day = importlib.import_module("day{:02d}".format(args["<day>"]))

    print(day.part1(entries))
    print(day.part2(entries))
