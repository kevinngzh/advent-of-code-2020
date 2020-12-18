import pytest

from .__init__ import evaluate_new_math, evaluate_new_advanced_math


examples = [
    ("1 + 2 * 3 + 4 * 5 + 6", (71, 231)),
    ("1 + (2 * 3) + (4 * (5 + 6))", (51, 51)),
    ("2 * 3 + (4 * 5)", (26, 46)),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", (437, 1445)),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", (12240, 669060)),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", (13632, 23340)),
]


@pytest.mark.parametrize("raw_example,expected", examples)
def test_evaluate_new_math(raw_example, expected):
    assert evaluate_new_math(raw_example) == expected[0]


@pytest.mark.parametrize("raw_example,expected", examples)
def test_evaluate_new_advanced_math(raw_example, expected):
    assert evaluate_new_advanced_math(raw_example) == expected[1]
