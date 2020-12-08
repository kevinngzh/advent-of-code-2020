import pytest

from .__init__ import parse_input, part1


@pytest.fixture
def example():
    raw_example = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 5


def test_part2(example):
    pass
