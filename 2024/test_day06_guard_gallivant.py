import pytest
import day06_guard_gallivant as day6


EXAMPLE_INPUT = """
....#.....
.....O...#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
EXAMPLE_GRIDSIZE = (10, 10)
EXAMPLE_START = (4, 6)
EXAMPLE_OBSTACLES = [(0, 8), (1, 6), (2, 3), (4, 0), (6, 9), (7, 4), (8, 7), (9, 1)]
EXAMPLE_RESULT = 41
EXAMPLE_RESULT_LOOP = 6
EXAMPLE_LOOP_OBS = {(3, 6), (6, 7), (7, 7), (1, 8), (3, 8), (7, 9)}


def test_read_input():
    gridsize, start, obstacles = day6.read_input(EXAMPLE_INPUT)
    assert gridsize == (10, 10)
    assert start == EXAMPLE_START
    print(obstacles)
    assert set(obstacles) == set(EXAMPLE_OBSTACLES)


def test_obstacle_class():
    """
     0123456
    0......#
    1.#...#.
    2......#
    3.......
    4.#....#
    5.......
    """
    obs = day6.Obstacles([(1, 1), (5, 1), (1, 4), (6, 0), (6, 2), (6, 4)])
    assert obs.next((0, 1), (1, 0)) == (1, 1)
    assert obs.next((1, 0), (0, 1)) == (1, 1)
    assert obs.next((3, 1), (-1, 0)) == (1, 1)
    assert obs.next((3, 1), (1, 0)) == (5, 1)
    assert obs.next((1, 3), (0, -1)) == (1, 1)
    assert obs.next((1, 3), (0, 1)) == (1, 4)

    assert obs.next((0, 1), (-1, 0)) is None
    assert obs.next((1, 0), (0, -1)) is None
    assert obs.next((1, 7), (1, 0)) is None
    assert obs.next((7, 1), (0, 1)) is None
    assert obs.next((3, 3), (0, 1)) is None

    assert obs.next((6, 1), (0, -1)) == (6, 0)
    assert obs.next((6, 1), (0, 1)) == (6, 2)
    assert obs.next((6, 3), (0, -1)) == (6, 2)
    assert obs.next((6, 3), (0, 1)) == (6, 4)
    assert obs.next((6, 5), (0, -1)) == (6, 4)
    assert obs.next((6, 5), (0, 1)) is None


def test_visit_count():
    steps = day6.visit_count_of_trip(EXAMPLE_GRIDSIZE, EXAMPLE_START, EXAMPLE_OBSTACLES)
    assert steps == EXAMPLE_RESULT


def test_loop_obs():
    loop_obs = day6.possible_loop_obstacles(
        EXAMPLE_GRIDSIZE, EXAMPLE_START, EXAMPLE_OBSTACLES
    )
    assert loop_obs == EXAMPLE_LOOP_OBS


def test_loop_count():
    loops = day6.possible_loop_count(EXAMPLE_GRIDSIZE, EXAMPLE_START, EXAMPLE_OBSTACLES)
    assert loops == EXAMPLE_RESULT_LOOP
