import pytest

from .__init__ import parse_input, part1, part2


@pytest.fixture
def example():
    raw_example = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 2


def test_part2(example):
    pass
