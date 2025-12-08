import day06_trash_compactor as day6


EXAMPLE_INPUT = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
EXAMPLE_RESULT = 4277556
EXAMPLE_RESULT_PART2 = 3263827


def test_example():
    nums, ops = day6.read_input(EXAMPLE_INPUT)
    assert day6.domath(nums, ops) == EXAMPLE_RESULT


def test_example_part2():
    cols, ops = day6.read_input_part2(EXAMPLE_INPUT)
    assert day6.docolmath(cols, ops) == EXAMPLE_RESULT_PART2
