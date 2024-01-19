import pytest
import day17_clumsy_crucible as day17


SAMPLE_INPUT = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

SAMPLE_INPUT_B = """
111111111111
999999999991
999999999991
999999999991
999999999991
"""


def test_minimize_part1():
    blocks = day17.read_input(SAMPLE_INPUT)
    heatloss = day17.minimize(blocks)
    assert heatloss == 102


def test_minimize_part2a():
    blocks = day17.read_input(SAMPLE_INPUT)
    heatloss = day17.minimize(blocks, pathmin=4, pathmax=10)
    assert heatloss == 94


def test_minimize_part2b():
    blocks = day17.read_input(SAMPLE_INPUT_B)
    heatloss = day17.minimize(blocks, pathmin=4, pathmax=10)
    assert heatloss == 71

@pytest.mark.longrun
@pytest.mark.puzzle
def test_day17_part1(benchmark):
    assert benchmark(day17.part1) == 1065

@pytest.mark.longrun
@pytest.mark.puzzle
def test_day17_part2(benchmark):
    assert benchmark(day17.part2) == 1249
