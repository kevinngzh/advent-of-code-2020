def parse_ranges(raw_ranges):
    ranges = []

    contiguous_ranges = raw_ranges.split(" or ")

    for raw_range in contiguous_ranges:
        first, last = raw_range.split("-")

        ranges.append((int(first), int(last)))

    return ranges


def parse_rules(raw_rules):
    rules = {}

    for line in raw_rules.split("\n"):
        key, raw_values = line.split(": ")
        rules[key] = parse_ranges(raw_values)

    return rules


def parse_ticket(line):
    return [int(i) for i in line.split(",")]


def parse_input(input_):
    raw_rules, raw_your_ticket, raw_nearby_tickets = input_.split("\n\n")

    rules = parse_rules(raw_rules)
    your_ticket = parse_ticket(raw_your_ticket.split("\n")[1])
    nearby_tickets = [parse_ticket(line) for line in raw_nearby_tickets.split("\n")[1:]]

    return rules, your_ticket, nearby_tickets


class TicketValidator:
    def __init__(self, rules):
        self.rules = rules

    def is_any_valid(self, value):
        for valid_ranges in self.rules.values():
            if self.is_valid(valid_ranges, value):
                return True

        return False
 
    @staticmethod
    def is_valid(ranges, value):
        for first, last in ranges:
            if first <= value <= last:
                return True

        return False


def part1(input_):
    rules, _, nearby_tickets = input_
    error_rate = 0

    validator = TicketValidator(rules)

    for ticket in nearby_tickets:
        for value in ticket:
            if not validator.is_any_valid(value):
                error_rate += value

    return error_rate


def part2(entries):
    pass
