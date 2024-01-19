import pytest
from day02_cube_conundrum import to_rgb, game_index, is_possible, min_possible
from day02_cube_conundrum import part1, part2


def test_rbg():
    assert to_rgb('1 red, 132 green') == [1, 132, 0]
    assert to_rgb("3 blue") == [0, 0, 3]
    assert to_rgb("8 red, 2 green, 1 blue") == [8, 2, 1]


def test_index():
    assert game_index("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 1
    assert game_index("Game 99: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 99


def test_is_possible():
    assert is_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert is_possible("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    assert ~is_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert ~is_possible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    assert is_possible("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    assert ~is_possible("Game 90: 14 blue, 10 red, 2 green; 11 blue, 3 red, 1 green; 5 blue, 2 green, 14 red")


def test_min_possible():
    assert min_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == [4, 2, 6]
    assert min_possible("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == [1, 3, 4]
    assert min_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == [20, 13, 6]
    assert min_possible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == [14, 3, 15]
    assert min_possible("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == [6, 3, 2]
    assert (min_possible("Game 90: 14 blue, 10 red, 2 green; 11 blue, 3 red, 1 green; 5 blue, 2 green, 14 red")
            == [14, 2, 14])


@pytest.mark.puzzle
def test_day02_part1(benchmark):
    assert benchmark(part1) == 2512


@pytest.mark.puzzle
def test_day02_part2(benchmark):
    assert benchmark(part2) == 67335
