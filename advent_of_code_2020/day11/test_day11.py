import pytest

from .__init__ import parse_input, part1, SeatLayout


raw_examples = [
"""
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""",
"""
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""",
"""
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
""",
"""
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
""",
"""
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
""",
"""
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
""",
]


@pytest.fixture
def examples():
    return [parse_input(raw_example.strip()) for raw_example in raw_examples]


def test_seat_layout(examples):
    seat_layout = SeatLayout(examples[0])

    assert seat_layout.max_x == 10
    assert seat_layout.max_y == 10


@pytest.mark.xfail
def test_seat_layout_str(examples):
    for i, state in enumerate(examples):
        seat_layout = SeatLayout(state)

        assert str(seat_layout) == raw_examples[i]


def test_state_changes(examples):
    initial, *next_states = examples
    seat_layout = SeatLayout(initial)

    for next_state in next_states:
        seat_layout.next_grid()

        assert seat_layout.grid == next_state


def test_part1(examples):
    result = part1(examples[0])

    assert result == 37
