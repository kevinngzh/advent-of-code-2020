import pytest

from .__init__ import parse_input, part1, part2


@pytest.fixture
def example():
    raw_example = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""

    return parse_input(raw_example.strip())


def test_group_any_yes_answer(example):
    assert len(example[0].all_answers) == 3
    assert len(example[1].all_answers) == 3
    assert len(example[2].all_answers) == 3
    assert len(example[3].all_answers) == 1
    assert len(example[4].all_answers) == 1


def test_part1(example):
    result = part1(example)

    assert result == 11


def test_group_only_yes_answer(example):
    assert len(example[0].yes_answers) == 3
    assert len(example[1].yes_answers) == 0
    assert len(example[2].yes_answers) == 1
    assert len(example[3].yes_answers) == 1
    assert len(example[4].yes_answers) == 1


def test_part2(example):
    result = part2(example)

    assert result == 6
