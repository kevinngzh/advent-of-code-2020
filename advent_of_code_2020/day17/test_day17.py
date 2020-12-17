import pytest

from .__init__ import parse_input, part1, part2


@pytest.fixture
def example():
    raw_example = """
.#.
..#
###
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 112


def test_part2(example):
    result = part2(example)

    assert result == 848
