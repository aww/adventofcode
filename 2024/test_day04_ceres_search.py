import pytest
import day04_ceres_search as day4


EXAMPLE_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

EXAMPLE_COORD = [
    (4, 0),
    (5, 0),
    (4, 1),
    (9, 3),
    (9, 3),
    (0, 4),
    (6, 4),
    (6, 4),
    (0, 5),
    (6, 5),
    (1, 9),
    (3, 9),
    (3, 9),
    (5, 9),
    (5, 9),
    (5, 9),
    (9, 9),
    (9, 9),
]

EXAMPLE_COORD_X = [
    (2, 1),
    (6, 2),
    (7, 2),
    (2, 3),
    (4, 3),
    (1, 7),
    (3, 7),
    (5, 7),
    (7, 7),
]


def test_find_xmas():
    count = 0
    s = day4.read_input(EXAMPLE_INPUT)
    for a, b in zip(day4.find_xmas(s), EXAMPLE_COORD):
        print(a, b)
        assert a == b
        count += 1
    assert count == len(EXAMPLE_COORD)


def test_find_x_mas():
    count = 0
    s = day4.read_input(EXAMPLE_INPUT)
    for a, b in zip(day4.find_x_mas(s), EXAMPLE_COORD_X):
        print(a, b)
        assert a == b
        count += 1
    assert count == len(EXAMPLE_COORD_X)
