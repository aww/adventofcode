import day04_printing_department as day4


EXAMPLE_INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
EXAMPLE_RESULT = 13
EXAMPLE_RESULT_PART2 = 43


def test_accessible_rolls():
    input = day4.read_input(EXAMPLE_INPUT)
    assert day4.accessible_rolls(input) == EXAMPLE_RESULT


def test_removable_rolls():
    input = day4.read_input(EXAMPLE_INPUT)
    assert day4.removable_rolls(input) == EXAMPLE_RESULT_PART2
