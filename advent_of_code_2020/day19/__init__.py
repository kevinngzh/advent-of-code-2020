def parse_rule(raw_rule):
    key, rule = raw_rule.split(': ')

    if '"' in rule:
        rule = rule.strip('"')
    else:
        subrules = []

        for raw_subrule in rule.split(" | "):
            subrules.append(tuple(int(i) for i in raw_subrule.split(" ")))

        rule = subrules

    return int(key), rule


def parse_input(input_):
    raw_rules, raw_messages = input_.split("\n\n")
    rules = [parse_rule(raw_rule) for raw_rule in raw_rules.split("\n")]

    return rules, raw_messages.split("\n")


class RuleValidator:
    def __init__(self, rules):
        self.rules = dict(rules)
        self.rules_len = {}

    def generate_rules_len(self, key):
        subrules_len = []

        for subrule in self.rules[key]:
            if isinstance(subrule, str):
                subrules_len.append(len(subrule))
            else:
                subrules_len.append(sum(self.get_rules_len(key) for key in subrule))

        assert all(length == subrules_len[0] for length in subrules_len)

        return subrules_len[0]

    def get_rules_len(self, key):
        if key not in self.rules_len:
            self.rules_len[key] = self.generate_rules_len(key)

        return self.rules_len[key]

    def is_valid(self, key, value):
        results = []

        if self.get_rules_len(key) != len(value):
            return False

        for subrule in self.rules[key]:
            if isinstance(subrule, str):
                results.append(subrule == value)
            else:
                subrule_results = []
                value_idx = 0

                for subkey in subrule:
                    last = value_idx + self.get_rules_len(subkey)

                    subrule_results.append(self.is_valid(subkey, value[value_idx:last]))

                    value_idx = last

                results.append(all(subrule_results))

        return any(results)


def part1(data):
    rules, messages = data

    validator = RuleValidator(rules)

    return sum(validator.is_valid(0, message) for message in messages)


def part2(entries):
    pass
