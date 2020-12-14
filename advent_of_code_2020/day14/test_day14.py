import pytest

from .__init__ import parse_input, part1, part2


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


def test_part2():
    raw_example = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

    result = part2(parse_input(raw_example.strip()))

    assert result == 208
