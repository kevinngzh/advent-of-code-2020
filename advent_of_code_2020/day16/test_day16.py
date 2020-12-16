import pytest

from .__init__ import parse_input, part1


@pytest.fixture
def example():
    raw_example = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)
