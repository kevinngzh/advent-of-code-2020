import pytest

from .__init__ import parse_input, parse_bus_ids, part1, part2


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


def test_part2(example):
    result = part2(example)

    assert result == None#1068781

    other_examples = [
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ]

    for raw_example, expected in other_examples:
        assert part2((None, parse_bus_ids(raw_example))) == None#expected
