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
        for key in self.rules.keys():
            if self.is_valid(key, value):
                return True

        return False

    def is_valid_ticket(self, ticket):
        for value in ticket:
            if not self.is_any_valid(value):
                return False

        return True
 
    def is_valid(self, key, value):
        for first, last in self.rules[key]:
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


def get_possibilities(validator, tickets):
    keys = validator.rules.keys()
    possibilities = {key: list(range(len(keys))) for key in keys}

    for key, possibles in possibilities.items():
        for ticket in tickets:
            for possible in possibles:
                if not validator.is_valid(key, ticket[possible]):
                    possibles.remove(possible)

    return possibilities


def resolve_possibilities(possibilities):
    key_indices = {}

    while len(possibilities):
        sorted_keys = sorted(possibilities.keys(), key=lambda k: len(possibilities[k]))
        first_key = sorted_keys[0]

        if len(possibilities[first_key]) == 1:
            only_key_idx, = possibilities.pop(first_key)
            key_indices[first_key] = only_key_idx

            for key in sorted_keys[1:]:
                possibilities[key].remove(only_key_idx)
        else:
            key_indices.update(possibilities)
            break

    return key_indices


def part2(input_):
    rules, your_ticket, nearby_tickets = input_
    result = 1

    validator = TicketValidator(rules)

    valid_nearby_tickets = list(filter(lambda ticket: validator.is_valid_ticket(ticket), nearby_tickets))

    possibilities = get_possibilities(validator, valid_nearby_tickets)
    key_indices = resolve_possibilities(possibilities)
    
    departure_indices = [idx for key, idx in key_indices.items() if key.startswith("departure")]

    for idx in departure_indices:
        result *= your_ticket[idx]

    return result
