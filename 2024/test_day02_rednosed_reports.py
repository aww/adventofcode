import pytest
import day02_rednosed_reports as day2


EXAMPLE_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_is_safe():
    assert day2.is_report_safe([7, 6, 4, 2, 1]) == True
    assert day2.is_report_safe([1, 2, 7, 8, 9]) == False
    assert day2.is_report_safe([9, 7, 6, 2, 1]) == False
    assert day2.is_report_safe([1, 3, 2, 4, 5]) == False
    assert day2.is_report_safe([8, 6, 4, 4, 1]) == False
    assert day2.is_report_safe([1, 3, 6, 7, 9]) == True


def test_eliminate_element():
    assert day2.eliminate_element([1, 3, 2, 4, 5], 2) == [1, 3, 4, 5]
    assert day2.eliminate_element([1, 3, 2, 4, 5], 0) == [3, 2, 4, 5]
    assert day2.eliminate_element([1, 3, 2, 4, 5], 4) == [1, 3, 2, 4]


def test_is_unsafe_dampened():
    assert day2.is_report_safe_dampened([7, 6, 4, 2, 1]) == True
    assert day2.is_report_safe_dampened([1, 2, 7, 8, 9]) == False
    assert day2.is_report_safe_dampened([9, 7, 6, 2, 1]) == False
    assert day2.is_report_safe_dampened([1, 3, 2, 4, 5]) == True
    assert day2.is_report_safe_dampened([8, 6, 4, 4, 1]) == True
    assert day2.is_report_safe_dampened([1, 3, 6, 7, 9]) == True
