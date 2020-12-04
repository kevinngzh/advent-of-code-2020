class Passport:
    FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    def __init__(self, data):
        parsed_data = self._parse_data(data)

        self.byr = parsed_data.get("byr", None)
        self.iyr = parsed_data.get("iyr", None)
        self.eyr = parsed_data.get("eyr", None)
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
            elif getattr(self, field) is None:
                return False

        return True


def parse_input(input_):
    passports = [Passport(passport_data) for passport_data in input_.split("\n\n")]

    return passports


def part1(passports):
    return sum(passport.is_valid(["cid"]) for passport in passports)


def part2(entries):
    pass
