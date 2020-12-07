

class GroupAnswer:
    def __init__(self, person_answers):
        self.person_answers = person_answers

    @property
    def yes_answers(self):
        return set(answer for answers in self.person_answers for answer in answers)


def parse_input(input_):
    return [GroupAnswer(group_answer.split("\n")) for group_answer in input_.split("\n\n")]


def part1(group_answers):
    return sum(len(group.yes_answers) for group in group_answers)


def part2(entries):
    pass
