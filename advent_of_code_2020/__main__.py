"""
Advent of Code 2020 solutions.

Usage:
    advent_of_code_2020 <input_file>
    advent_of_code_2020 day <day> <input_file>
    advent_of_code_2020 -h | --help
    advent_of_code_2020 --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""


__version__ = "0.1.5"


import re
import sys

from docopt import docopt
from schema import Schema, Or, Use


def _get_latest_day():
    pattern = re.compile("day(\d+)$")
    days = []

    for path in os.listdir("advent_of_code_2020"):
        match = pattern.search(path)

        if match is not None:
            days.append(int(match.group(1)))

    return max(days)


if __name__ == "__main__":
    import importlib
    import os

    s = Schema({
        "<day>": Or(None, Use(int)),
        "<input_file>": Use(open),
    }, ignore_extra_keys=True)

    args = s.validate(docopt(__doc__, version=__version__))

    entries = [int(i) for i in args["<input_file>"].readlines()]

    day = args["<day>"] or _get_latest_day()
    day = importlib.import_module("day{:02d}".format(day))

    print(day.part1(entries))
    print(day.part2(entries))
