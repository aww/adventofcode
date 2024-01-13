import numpy as np
from day14_parabolic_reflector_dish import read_input, tilt_north, rot, calc_north_load, spincycle, applyspincycles, stats


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
    assert (tilt_north(read_input(TEST_SAMPLE_A)) == read_input(TEST_SAMPLE_A_TILTED)).all()


def test_rotate():
    tst = np.array([[0, 0, 1, 0], [2, 1, 1, 1], [0, 0, 1, 2], [2, 0, 0, 1]])
    tstrot = np.array([[2, 0, 2, 0], [0, 0, 1, 0], [0, 1, 1, 1], [1, 2, 1, 0]])
    assert (rot(tst) == tstrot).all()


def test_calc_north_load():
    assert calc_north_load(read_input(TEST_SAMPLE_A_TILTED)) == 136


def test_cycle():
    rocks = read_input(TEST_SAMPLE_A)
    cycle1 = spincycle(rocks)
    assert (cycle1 == read_input(TEST_SAMPLE_A_CYCLE1)).all()
    cycle2 = spincycle(cycle1)
    assert (cycle2 == read_input(TEST_SAMPLE_A_CYCLE2)).all()
    cycle3 = spincycle(cycle2)
    assert (cycle3 == read_input(TEST_SAMPLE_A_CYCLE3)).all()


def test_applyspincycles():
    rocks = read_input(TEST_SAMPLE_A)
    rocks = applyspincycles(rocks, n=1000000000)
    assert stats(rocks)['load'] == 64
