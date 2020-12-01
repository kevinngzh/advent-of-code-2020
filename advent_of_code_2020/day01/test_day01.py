import pytest

from .__init__ import part1, part2


@pytest.fixture
def example():
    raw_example = """
1721
979
366
299
675
1456
"""

    return [int(i) for i in raw_example.strip().split("\n")]


def test_part1(example):
    result = part1(example)
    pair = frozenset((1721, 299))

    assert pair in result
    assert result[pair] == 514579


def test_part2(example):
    result = part2(example)
    trip = frozenset((979, 366, 675))

    assert trip in result
    assert result[trip] == 241861950
