import day03_lobby as day3


EXAMPLE_INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
EXAMPLE_RESULT = 357
EXAMPLE_RESULT_PART2 = 3121910778619


def test_max_joltage():
    assert day3.max_joltage("987654321111111") == 98
    assert day3.max_joltage("811111111111119") == 89
    assert day3.max_joltage("234234234234278") == 78
    assert day3.max_joltage("818181911112111") == 92


def test_example():
    input = day3.read_input(EXAMPLE_INPUT)
    assert day3.total_joltage(input) == EXAMPLE_RESULT


def test_max_joltage_sized():
    assert day3.max_joltage_sized("987654321111111", 12) == 987654321111
    assert day3.max_joltage_sized("811111111111119", 12) == 811111111119
    assert day3.max_joltage_sized("234234234234278", 12) == 434234234278
    assert day3.max_joltage_sized("818181911112111", 12) == 888911112111


def test_example_part2():
    input = day3.read_input(EXAMPLE_INPUT)
    assert day3.total_joltage_twelve(input) == EXAMPLE_RESULT_PART2
