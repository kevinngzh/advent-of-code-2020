import pytest

from .__init__ import parse_input, part1


@pytest.fixture
def example():
    raw_example = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 2
