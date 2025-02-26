import pytest
import day01_historian_hysteria as day1


EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

EXAMPLE_LISTS = [
    [3, 4, 2, 1, 3, 3],
    [4, 3, 5, 3, 9, 3],
]

SAMPLE_INPUT = """
47078   87818
99261   15906
44723   23473
87598   26876
"""


def test_input():
    a, b = day1.read_input(EXAMPLE_INPUT)
    assert a == EXAMPLE_LISTS[0]
    assert b == EXAMPLE_LISTS[1]
    a, b = day1.read_input(SAMPLE_INPUT)
    assert a == [47078, 99261, 44723, 87598]
    assert b == [87818, 15906, 23473, 26876]


def test_part1():
    d = day1.distance(*EXAMPLE_LISTS)
    assert d == 11


def test_part2():
    s = day1.similarity(*EXAMPLE_LISTS)
    assert s == 31
