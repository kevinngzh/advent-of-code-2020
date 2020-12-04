import re


class Passport:
    FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    VALID_BYRS = (1920, 2002)
    VALID_IYRS = (2010, 2020)
    VALID_EYRS = (2020, 2030)
    VALID_HGTS = {
        "pattern": r"(\d*?)(cm|in)$",
        "cm": (150, 193),
        "in": (59, 76),
    }
    VALID_HCLS = r"#[0-9a-f]{6}$"
    VALID_ECLS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def __init__(self, data):
        parsed_data = self._parse_data(data)
        intize = lambda key: int(parsed_data[key]) if key in parsed_data else None

        self.byr = intize("byr")
        self.iyr = intize("iyr")
        self.eyr = intize("eyr")
        self.hgt = parsed_data.get("hgt", None)
        self.hcl = parsed_data.get("hcl", None)
        self.ecl = parsed_data.get("ecl", None)
        self.pid = parsed_data.get("pid", None)
        self.cid = parsed_data.get("cid", None)

    def _parse_data(self, data):
        data = data.replace("\n", " ")
        fields = data.split(" ")
        parsed_data = {}

        for key_value in fields:
            key, value = key_value.split(":")
            parsed_data[key] = value

        return parsed_data

    def is_valid(self, optional=None):
        for field in self.FIELDS:
            if optional and field in optional:
                continue

            value = getattr(self, field)

            if value is None:
                return False
            elif getattr(self, f"is_valid_{field}")(value) is False:
                return False

        return True

    @staticmethod
    def is_value_in_range(rng, value):
        return rng[0] <= value <= rng[1]

    @classmethod
    def is_valid_byr(cls, value):
        return cls.is_value_in_range(cls.VALID_BYRS, value)

    @classmethod
    def is_valid_iyr(cls, value):
        return cls.is_value_in_range(cls.VALID_IYRS, value)

    @classmethod
    def is_valid_eyr(cls, value):
        return cls.is_value_in_range(cls.VALID_EYRS, value)

    @classmethod
    def is_valid_hgt(cls, value):
        condition = cls.VALID_HGTS
        match = re.match(condition["pattern"], value)

        if match is not None:
            value, unit = match.groups()
            min_, max_ = condition[unit]

            return min_ <= int(value) <= max_

        return False

    @classmethod
    def is_valid_hcl(cls, value):
        return re.match(cls.VALID_HCLS, value) is not None

    @classmethod
    def is_valid_ecl(cls, value):
        return value in cls.VALID_ECLS

    @staticmethod
    def is_valid_pid(value):
        return len(value) == 9 and value.isdigit()

    @staticmethod
    def is_valid_cid(value):
        return True


def parse_input(input_):
    passports = [Passport(passport_data) for passport_data in input_.split("\n\n")]

    return passports


def part1(passports):
    return sum(passport.is_valid(["cid"]) for passport in passports)


def part2(passports):
    pass
