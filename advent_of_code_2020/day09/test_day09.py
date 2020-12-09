import pytest

from .__init__ import parse_input, part1


@pytest.fixture
def example():
    raw_example = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example, 5)

    assert result == 127
