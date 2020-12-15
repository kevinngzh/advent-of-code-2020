import pytest

from .__init__ import parse_input, part1, part2


examples = [
    ("0,3,6", (436, 175594)),
    ("1,3,2", (1, 2578)),
    ("2,1,3", (10, 3544142)),
    ("1,2,3", (27, 261214)),
    ("2,3,1", (78, 6895259)),
    ("3,2,1", (438, 18)),
    ("3,1,2", (1836, 362)),
]


@pytest.mark.parametrize("raw_example,expected", examples)
def test_part1(raw_example, expected):
    assert part1(parse_input(raw_example)) == expected[0]


@pytest.mark.parametrize("raw_example,expected", examples)
def test_part2(raw_example, expected):
    assert part2(parse_input(raw_example)) == expected[1]
