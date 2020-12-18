from collections import defaultdict


def parse_input(input_):
    return input_.split("\n")


def evaluate_new_math(expression):
    bracket_levels = defaultdict(int)
    current_bracket_level = 0

    while "(" in expression:
        for idx, char in enumerate(expression):
            if char == "(":
                current_bracket_level += 1
                bracket_levels[current_bracket_level] = idx
            if char == ")":
                lbracket = bracket_levels[current_bracket_level]
                rbracket = idx + 1

                nested = expression[lbracket : rbracket]

                expression = expression[:lbracket] + str(evaluate_new_math(nested[1:-1])) + expression[rbracket:]
                current_bracket_level -= 1

                break

    symbols = expression.split(" ")
    operator = "+"
    result = 0

    for symbol in symbols:
        if symbol in "+*":
            operator = symbol
        else:
            if operator == "+":
                result += int(symbol)
            elif operator == "*":
                result *= int(symbol)

    return result


def evaluate_new_advanced_math(expression):
    bracket_levels = defaultdict(int)
    current_bracket_level = 0

    while "(" in expression:
        for idx, char in enumerate(expression):
            if char == "(":
                current_bracket_level += 1
                bracket_levels[current_bracket_level] = idx
            if char == ")":
                lbracket = bracket_levels[current_bracket_level]
                rbracket = idx + 1

                nested = expression[lbracket : rbracket]

                expression = expression[:lbracket] + str(evaluate_new_advanced_math(nested[1:-1])) + expression[rbracket:]
                current_bracket_level -= 1

                break

    symbols = expression.split(" ")
    operator = "+"
    result = 0

    while "+" in symbols:
        add_idx = symbols.index("+")
        lnum = add_idx - 1
        rnum = add_idx + 1

        symbols = symbols[:lnum] + [str(int(symbols[lnum]) + int(symbols[rnum]))] + symbols[rnum+1:]

    for symbol in symbols:
        if symbol in "+*":
            operator = symbol
        else:
            if operator == "+":
                result += int(symbol)
            elif operator == "*":
                result *= int(symbol)

    return result


def part1(expressions):
    return sum(evaluate_new_math(expression) for expression in expressions)


def part2(expressions):
    return sum(evaluate_new_advanced_math(expression) for expression in expressions)
