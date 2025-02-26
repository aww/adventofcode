import pytest
import day07_bridge_repair as day7


EXAMPLE_INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
EXAMPLE_RESULT1 = 3749
EXAMPLE_RESULT2 = 11387


def test_total_calibration_result():
    equations = day7.read_input(EXAMPLE_INPUT)
    assert day7.total_calibration_result(equations) == EXAMPLE_RESULT1


def test_total_calibration_result2():
    equations = day7.read_input(EXAMPLE_INPUT)
    assert day7.total_calibration_result2(equations) == EXAMPLE_RESULT2
