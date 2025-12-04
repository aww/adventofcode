import day01_secret_entrance as day1


EXAMPLE_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
EXAMPLE_RESULT_AT = 3
EXAMPLE_RESULT_CLICK = 6


def test_at():
    input = day1.read_input(EXAMPLE_INPUT)
    assert day1.count_at_zero(input) == EXAMPLE_RESULT_AT


def test_click():
    input = day1.read_input(EXAMPLE_INPUT)
    assert day1.count_click_zero(input) == EXAMPLE_RESULT_CLICK


def test_variant_a():
    input = day1.read_input("R450")
    assert day1.count_click_zero(input) == 5


def test_variant_b():
    input = day1.read_input("L450")
    assert day1.count_click_zero(input) == 5
