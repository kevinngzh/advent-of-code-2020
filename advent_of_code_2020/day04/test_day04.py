import pytest

from .__init__ import parse_input, part1, part2, Passport


@pytest.fixture
def example():
    raw_example = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

    return parse_input(raw_example.strip())


def test_part1(example):
    result = part1(example)

    assert result == 2


def test_passport_byr():
    assert Passport.is_valid_byr(2002) is True
    assert Passport.is_valid_byr(2003) is False


def test_passport_hgt():
    assert Passport.is_valid_hgt("60in") is True
    assert Passport.is_valid_hgt("190cm") is True
    assert Passport.is_valid_hgt("190in") is False
    assert Passport.is_valid_hgt("190") is False


def test_passport_hcl():
    assert Passport.is_valid_hcl("#123abc") is True
    assert Passport.is_valid_hcl("#123abz") is False
    assert Passport.is_valid_hcl("123abc") is False


def test_passport_ecl():
    assert Passport.is_valid_ecl("brn") is True
    assert Passport.is_valid_ecl("wat") is False


def test_passport_pid():
    assert Passport.is_valid_pid("000000001") is True
    assert Passport.is_valid_pid("0123456789") is False


def test_valid_passports():
    invalid_raw_examples = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""
    valid_raw_examples = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

    invalid_examples = parse_input(invalid_raw_examples.strip())
    valid_examples = parse_input(valid_raw_examples.strip())

    for example in invalid_examples:
        assert example.is_strict_valid(["cid"]) is False

    for example in valid_examples:
        assert example.is_strict_valid(["cid"]) is True
