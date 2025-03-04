import day11_plutonian_pebbles as day11


EXAMPLE_INPUT = "0 1 10 99 999"
EXAMPLE_BLINK1 = [1, 2024, 1, 0, 9, 9, 2021976]
EXAMPLE_BLINK1_RESULT = 7

EXAMPLE2_INPUT = "125 17"
EXAMPLE2_BLINK1 = [253000, 1, 7]
EXAMPLE2_BLINK2 = [253, 0, 2024, 14168]
EXAMPLE2_BLINK3 = [512072, 1, 20, 24, 28676032]
EXAMPLE2_BLINK4 = [512, 72, 2024, 2, 0, 2, 4, 2867, 6032]
EXAMPLE2_BLINK5 = [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32]
EXAMPLE2_BLINK6 = [
    2097446912,
    14168,
    4048,
    2,
    0,
    2,
    4,
    40,
    48,
    2024,
    40,
    48,
    80,
    96,
    2,
    8,
    6,
    7,
    6,
    0,
    3,
    2,
]
EXAMPLE2_BLINK1_RESULT = 3
EXAMPLE2_BLINK2_RESULT = 4
EXAMPLE2_BLINK3_RESULT = 5
EXAMPLE2_BLINK4_RESULT = 9
EXAMPLE2_BLINK5_RESULT = 13
EXAMPLE2_BLINK6_RESULT = 22


def test_blink():
    input = day11.read_input(EXAMPLE_INPUT)
    assert day11.blink(input) == EXAMPLE_BLINK1


def test_blinkcount():
    input = day11.read_input(EXAMPLE_INPUT)
    assert day11.blinkcountsum(input, 1) == EXAMPLE_BLINK1_RESULT


def test_blinkcount2():
    input = day11.read_input(EXAMPLE2_INPUT)
    assert day11.blinkcountsum(input, 1) == EXAMPLE2_BLINK1_RESULT
    assert day11.blinkcountsum(input, 2) == EXAMPLE2_BLINK2_RESULT
    assert day11.blinkcountsum(input, 3) == EXAMPLE2_BLINK3_RESULT
    assert day11.blinkcountsum(input, 4) == EXAMPLE2_BLINK4_RESULT
    assert day11.blinkcountsum(input, 5) == EXAMPLE2_BLINK5_RESULT
    assert day11.blinkcountsum(input, 6) == EXAMPLE2_BLINK6_RESULT


def test_blink2():
    input = day11.read_input(EXAMPLE2_INPUT)
    b1 = day11.blink(input)
    assert b1 == EXAMPLE2_BLINK1
    b2 = day11.blink(b1)
    assert b2 == EXAMPLE2_BLINK2
    b3 = day11.blink(b2)
    assert b3 == EXAMPLE2_BLINK3
    b4 = day11.blink(b3)
    assert b4 == EXAMPLE2_BLINK4
    b5 = day11.blink(b4)
    assert b5 == EXAMPLE2_BLINK5
    b6 = day11.blink(b5)
    assert b6 == EXAMPLE2_BLINK6
