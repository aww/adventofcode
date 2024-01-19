import pytest
from day03_gear_ratios import preformat, find_adjacent_numbers, find_integer_from, find_integers_centered
from day03_gear_ratios import find_gear_pairs, part1, part2


def test_find_adjacent_numbers():
    sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    # This simulates file.readlines()
    sample_readlines = sample.splitlines(keepends=True)
    sample_readlines = preformat(sample_readlines)
    yes, no = find_adjacent_numbers(sample_readlines)
    assert set([x[0] for x in yes]) == {467, 35, 633, 617, 592, 755, 664, 598}
    assert set([x[0] for x in no]) == {114, 58}


def test_find_integer_from():
    assert find_integer_from("....453...", 4) == 453
    assert find_integer_from("....453...", 5) == 453
    assert find_integer_from("....453...", 6) == 453
    assert find_integer_from("....453", 6) == 453
    assert find_integer_from("453......", 0) == 453
    assert find_integer_from("453......", 2) == 453


def test_find_integers_centered():
    assert find_integers_centered("...453.128........", 6) == [453, 128]
    assert find_integers_centered("...453.128........", 5) == [453]
    assert find_integers_centered("...453.128........", 7) == [128]
    assert find_integers_centered("...453.128........", 8) == [128]
    assert find_integers_centered("...453.128........", 9) == [128]
    assert find_integers_centered("...453.128........", 10) == [128]
    assert find_integers_centered("...453.128........", 11) == []


def test_find_gear_pairs():
    sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    # This simulates file.readlines()
    sample_readlines = sample.splitlines(keepends=True)
    sample_readlines = preformat(sample_readlines)
    pairs = find_gear_pairs(sample_readlines)
    assert ({frozenset([x[0], x[1]]) for x in pairs}
            == {frozenset([467, 35]), frozenset([755, 598])})


@pytest.mark.puzzle
def test_day03_part1(benchmark):
    assert benchmark(part1) == 507214


@pytest.mark.puzzle
def test_day03_part2(benchmark):
    assert benchmark(part2) == 72553319
