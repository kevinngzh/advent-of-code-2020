from collections import namedtuple
import re


Bag = namedtuple("Bag", ["adjective", "color"])


class LuggageRule:
    BAG_PATTERN = re.compile(r"(\d+ )?(\w+) (\w+) bag[s]?")

    def __init__(self, rule):
        self.bag, self.contains = self.parse_rule(rule)

    @classmethod
    def parse_bag(cls, bag):
        num, adjective, color = cls.BAG_PATTERN.match(bag).groups()

        if num is not None:
            num = int(num)

        return num, Bag(adjective, color)

    @classmethod
    def parse_rule(cls, rule):
        raw_bag, raw_contains = rule.split(" contain ")
        # Remove trailing period mark.
        raw_contains = raw_contains[:-1]

        _, bag = cls.parse_bag(raw_bag)
        contains = {}

        if raw_contains == "no other bags":
            contains = None
        else:
            for raw_contain_bag in raw_contains.split(", "):
                num, contain_bag = cls.parse_bag(raw_contain_bag)

                contains[contain_bag] = num

        return bag, contains


def parse_input(input_):
    return list(map(LuggageRule, input_.split("\n")))


def part1(luggage_rules):
    search_bag = Bag("shiny", "gold")
    to_search = luggage_rules.copy()
    searched = {}

    while len(to_search):
        current_rule = to_search.pop()
        
        if current_rule.contains is None:
            searched[current_rule.bag] = False
        elif search_bag in current_rule.contains:
            searched[current_rule.bag] = True
        elif all(bag in searched for bag in current_rule.contains):
            searched[current_rule.bag] = any(searched[bag] for bag in current_rule.contains)
        else:
            to_search.insert(0, current_rule)

    return sum(searched.values())


def get_bag_number(luggage_rules, bag):
    # Oops should have made `luggage_rules` a `dict`.
    bag_rule = [rule for rule in luggage_rules if rule.bag == bag]

    assert len(bag_rule) == 1
    bag_rule = bag_rule[0]

    if bag_rule.contains is None:
        return 0
    else:
        return sum((get_bag_number(luggage_rules, contains_bag) + 1) * bag_rule.contains[contains_bag] for contains_bag in bag_rule.contains)


def part2(luggage_rules):
    search_bag = Bag("shiny", "gold")

    return get_bag_number(luggage_rules, search_bag)
