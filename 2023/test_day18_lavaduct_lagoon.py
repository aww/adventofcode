import pytest
import day18_lavaduct_lagoon as day18


SAMPLE_INPUT = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


SAMPLE_CODED = [
    (0, 6),
    (1, 5),
    (2, 2),
    (1, 2),
    (0, 2),
    (1, 2),
    (2, 5),
    (3, 2),
    (2, 1),
    (3, 2),
    (0, 2),
    (3, 3),
    (2, 2),
    (3, 2),
]

SAMPLE_CODED_FIX = [
    (0, 461937),
    (1, 56407),
    (0, 356671),
    (1, 863240),
    (0, 367720),
    (1, 266681),
    (2, 577262),
    (3, 829975),
    (2, 112010),
    (1, 829975),
    (2, 491645),
    (3, 686074),
    (2, 5411),
    (3, 500254),
]


SAMPLE_B_CODED = [
    (2, 4),
    (1, 5),
    (0, 4),
    (3, 5),
]


SAMPLE_C_CODED = [
    (2, 4),
    (1, 10),
    (0, 4),
    (3, 5),
]

SAMPLE_D_CODED = [
    (0, 5),
    (1, 3),
    (2, 1),
    (1, 4),
    (0, 3),
    (3, 2),
    (0, 3),
    (3, 2),
    (2, 3),
    (3, 2),
    (0, 8),
    (1, 3),
    (2, 2),
    (1, 7),
    (2, 3),
    (3, 2),
    (2, 5),
    (1, 3),
    (0, 10),
    (1, 1),
    (2, 13),
    (3, 6),
    (2, 1),
    (3, 6),
    (2, 1),
    (3, 1),
]

#               111111
#     0123456789012345
#
#  0  ######..........  6
#  1  ##OOO#.#########  21
#  2  .#OOO#.#OOOOOOO#  35
#  3  .#OO##.####OOOO#  49
#  4  .#OO#.....#OO###  59
#  5  .#OO#..####OO#..  70
#  6  .#OO#..#OOOOO#..
#  7  .##O####OOOOO#..
#  8  ..#OOOOOOOOOO#..
#  9  ..#OO######OO#..
# 10  ..#OO#....#OO#..
# 11  ..#OO#....####..
# 12  ..#OO###########
# 13  ..##############
#
#  16*14=224 - 22 - 14 - 8 - 18 = 162
#
SAMPLE_DRAWN = """#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######"""

SAMPLE_CORNERS = {
    0: [(0, 0, 2), (6, 0, 5)],
    2: [(0, 0, 2), (2, 2, 5), (6, 0, 5)],
    5: [(0, 5, 7), (2, 2, 5), (4, 5, 7), (6, 0, 5)],
    7: [(0, 5, 7), (1, 7, 9), (4, 5, 7), (6, 7, 9)],
    9: [(1, 7, 9), (6, 7, 9)]
}

WIDTH_TIMES_DELTAY = [
    7,
    7 * 1,
    7,
    5 * 2,
    7,
    5 * 1,
    7,
    6 * 1,
    6
]

# def test_width_above_width():
#     assert day18.width_above_width(SAMPLE_CORNERS[0]) == (7, 0)
#     assert day18.width_above_width(SAMPLE_CORNERS[2]) == (7, 7)
#     assert day18.width_above_width(SAMPLE_CORNERS[5]) == (7, 5)
#     assert day18.width_above_width(SAMPLE_CORNERS[7]) == (7, 5)
#     assert day18.width_above_width(SAMPLE_CORNERS[9]) == (6, 6)


def test_draw():
    lineset, _, cols, rows = day18.normalized_lineset(SAMPLE_CODED)
    assert day18.draw(cols, rows, lineset) == SAMPLE_DRAWN


def test_is_closed():
    assert day18.is_closed(SAMPLE_CODED)
    assert day18.is_closed(SAMPLE_B_CODED)
    assert not day18.is_closed(SAMPLE_C_CODED)


def test_winding_number():
    assert day18.winding_number(SAMPLE_CODED) == 1
    assert day18.winding_number(SAMPLE_B_CODED) == -1


def test_read_input():
    assert day18.read_input(SAMPLE_INPUT) == SAMPLE_CODED


def test_read_input_fix():
    assert day18.read_input_fix(SAMPLE_INPUT) == SAMPLE_CODED_FIX


def test_interior_by_floodfill():
    plan = day18.read_input(SAMPLE_INPUT)
    winding = day18.winding_number(plan)
    lineset, interiorset, _, _ = day18.normalized_lineset(plan, winding=winding)
    interiorset = day18.interior_by_floodfill(lineset, interiorset)
    assert len(lineset) + len(interiorset) == 62


def test_area_by_rasterscan():
    # plan = day18.read_input(SAMPLE_INPUT)
    # xlist, ylist = day18.normalized_path(plan)
    # assert day18.area_by_rasterscan(xlist, ylist) == 62
    xlist, ylist = day18.normalized_path(SAMPLE_D_CODED)
    winding = day18.winding_number(SAMPLE_D_CODED)
    lineset, interiorset, cols, rows = day18.normalized_lineset(SAMPLE_D_CODED, winding=winding)
    print(day18.draw(cols, rows, lineset, interiorset))
    assert day18.area_by_rasterscan(xlist, ylist) == 162

@pytest.mark.puzzle
def test_day18_part1(benchmark):
    assert benchmark(day18.part1) == 49061

#
# @pytest.mark.puzzle
# def test_day18_part2(benchmark):
#     assert benchmark(day18.part2) == 0
