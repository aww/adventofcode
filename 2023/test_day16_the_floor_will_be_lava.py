import numpy as np
from day16_the_floor_will_be_lava import read_input, trace, traceall


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
    grid = read_input(SAMPLE_INPUT)
    energized = trace(grid)
    assert np.sum(energized) == 46


def test_traceall():
    grid = read_input(SAMPLE_INPUT)
    assert traceall(grid) == 51
