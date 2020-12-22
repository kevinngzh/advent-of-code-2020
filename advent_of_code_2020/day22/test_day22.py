import pytest

from .__init__ import parse_input, part1, part2


@pytest.fixture
def example():
    raw_example = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 306


def test_part2(example):
    result = part2(example)

    assert result == 291
