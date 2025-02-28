import day10_hoof_it as day10

EXAMPLE_INPUT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
EXAMPLE_RESULT = 36
EXAMPLE_RESULT_RATING = 81

EXAMPLE_INPUT_2 = """
9990559
9991598
9992557
6543456
7651987
8761111
9871111
"""
EXAMPLE_RESULT_2_RATING = 13

EXAMPLE_INPUT_3 = """
012345
123456
234567
345678
416789
567891
"""
EXAMPLE_RESULT_3_RATING = 227


def test_tailheadscoresum():
    input = day10.read_input(EXAMPLE_INPUT)
    assert day10.trailheadscoresum(input) == EXAMPLE_RESULT


def test_tailheadratingsum():
    input = day10.read_input(EXAMPLE_INPUT)
    assert day10.trailheadratingsum(input) == EXAMPLE_RESULT_RATING


def test_tailheadratingsum2():
    input = day10.read_input(EXAMPLE_INPUT_2)
    assert day10.trailheadratingsum(input) == EXAMPLE_RESULT_2_RATING


def test_tailheadratingsum3():
    input = day10.read_input(EXAMPLE_INPUT_3)
    assert day10.trailheadratingsum(input) == EXAMPLE_RESULT_3_RATING
