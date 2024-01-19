import pytest
import numpy as np
import day16_the_floor_will_be_lava as day16


SAMPLE_INPUT = """
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""


def test_trace():
    grid = day16.read_input(SAMPLE_INPUT)
    energized = day16.trace(grid)
    assert np.sum(energized) == 46


def test_traceall():
    grid = day16.read_input(SAMPLE_INPUT)
    assert day16.traceall(grid) == 51


@pytest.mark.puzzle
def test_day16_part1(benchmark):
    assert benchmark(day16.part1) == 8146


@pytest.mark.longrun
@pytest.mark.puzzle
def test_day16_part2(benchmark):
    assert benchmark(day16.part2) == 8358
