from .__init__ import parse_input, part1, part2


raw_example_1 = """
16
10
15
5
1
11
7
19
6
12
4
"""
raw_example_2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


example_1 = parse_input(raw_example_1.strip())
example_2 = parse_input(raw_example_2.strip())


def test_part1():
    assert part1(example_1) == 7 * 5
    assert part1(example_2) == 22 * 10


def test_part2():
    assert part2(example_1) == 8
    assert part2(example_2) == 19208
