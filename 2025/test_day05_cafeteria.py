import day05_cafeteria as day5


EXAMPLE_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
EXAMPLE_RESULT = 3
EXAMPLE_RESULT_PART2 = 14


def test_countfresh():
    ranges, available = day5.read_input(EXAMPLE_INPUT)
    assert day5.countfresh(ranges, available) == EXAMPLE_RESULT


def test_countallfresh():
    ranges, _ = day5.read_input(EXAMPLE_INPUT)
    assert day5.countallfresh(ranges) == EXAMPLE_RESULT_PART2
