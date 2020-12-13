import pytest

from .__init__ import parse_input, part1


@pytest.fixture
def example():
    raw_example = """
939
7,13,x,x,59,x,31,19
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 295
