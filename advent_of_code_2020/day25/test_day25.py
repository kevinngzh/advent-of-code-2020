import pytest

from .__init__ import parse_input, part1


@pytest.fixture
def example():
    raw_example = """
5764801
17807724
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 14897079
