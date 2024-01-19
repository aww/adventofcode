import pytest
from day06_wait_for_it import read_races, ways_to_beat, ways_to_beat_fast, part1, part2

SAMPLE_INPUT = """Time:      7  15   30
Distance:  9  40  200"""
SAMPLE_TUPLES = [(7, 9), (15, 40), (30, 200)]


def test_read_races():
    assert read_races(SAMPLE_INPUT) == SAMPLE_TUPLES


def test_ways_to_beat():
    assert [ways_to_beat(*r) for r in SAMPLE_TUPLES] == [4, 8, 9]


def test_ways_to_beat_fast():
    assert [ways_to_beat_fast(*r) for r in SAMPLE_TUPLES] == [4, 8, 9]
    assert ways_to_beat_fast(71530, 940200) == 71503


@pytest.mark.puzzle
def test_day06_part1(benchmark):
    assert benchmark(part1) == 6209190


@pytest.mark.puzzle
def test_day06_part2(benchmark):
    assert benchmark(part2) == 28545089
