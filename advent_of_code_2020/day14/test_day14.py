import pytest

from .__init__ import parse_input, part1


@pytest.fixture
def example():
    raw_example = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 165
