import pytest
import numpy as np
import day14_parabolic_reflector_dish as day14


TEST_SAMPLE_A = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


TEST_SAMPLE_A_TILTED = """
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
"""


TEST_SAMPLE_A_CYCLE1 = """
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
"""


TEST_SAMPLE_A_CYCLE2 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
"""


TEST_SAMPLE_A_CYCLE3 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
"""


def test_tilt_north():
    assert (day14.tilt_north(day14.read_input(TEST_SAMPLE_A)) == day14.read_input(TEST_SAMPLE_A_TILTED)).all()


def test_rotate():
    tst = np.array([[0, 0, 1, 0], [2, 1, 1, 1], [0, 0, 1, 2], [2, 0, 0, 1]])
    tstrot = np.array([[2, 0, 2, 0], [0, 0, 1, 0], [0, 1, 1, 1], [1, 2, 1, 0]])
    assert (day14.rot(tst) == tstrot).all()


def test_calc_north_load():
    assert day14.calc_north_load(day14.read_input(TEST_SAMPLE_A_TILTED)) == 136


def test_cycle():
    rocks = day14.read_input(TEST_SAMPLE_A)
    cycle1 = day14.spincycle(rocks)
    assert (cycle1 == day14.read_input(TEST_SAMPLE_A_CYCLE1)).all()
    cycle2 = day14.spincycle(cycle1)
    assert (cycle2 == day14.read_input(TEST_SAMPLE_A_CYCLE2)).all()
    cycle3 = day14.spincycle(cycle2)
    assert (cycle3 == day14.read_input(TEST_SAMPLE_A_CYCLE3)).all()


def test_applyspincycles():
    rocks = day14.read_input(TEST_SAMPLE_A)
    rocks = day14.applyspincycles(rocks, n=1000000000)
    assert day14.stats(rocks)['load'] == 64


@pytest.mark.puzzle
def test_day14_part1(benchmark):
    assert benchmark(day14.part1) == 105784


@pytest.mark.longrun
@pytest.mark.puzzle
def test_day14_part2(benchmark):
    assert benchmark(day14.part2) == 91286
