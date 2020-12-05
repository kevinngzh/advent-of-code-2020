from .__init__ import generate_seat_id


def test_part1():
    assert generate_seat_id("FBFBBFFRLR")[1:] == (44, 5, 357)
    assert generate_seat_id("BFFFBBFRRR")[1:] == (70, 7, 567)
    assert generate_seat_id("FFFBBBFRRR")[1:] == (14, 7, 119)
    assert generate_seat_id("BBFFBBFRLL")[1:] == (102, 4, 820)


def test_part2():
    pass
