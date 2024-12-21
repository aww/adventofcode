import pytest
import day03_mull_it_over as day3


EXAMPLE_INPUT = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
EXAMPLE_PAIRS = [(2,4), (5,5), (11,8), (8,5)]
EXAMPLE_SUM = 161
EXAMPLE_INPUT_DO_DONT = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
EXAMPLE_PAIRS_DO_DONT = [(2,4), (8,5)]
EXAMPLE_SUM_DO_DONT = 48

def test_scan_for_muls():
    count = 0
    for a, b in zip(day3.scan_for_muls(EXAMPLE_INPUT), EXAMPLE_PAIRS):
        assert a == b
        count += 1
    assert count == len(EXAMPLE_PAIRS)


def test_sumprod():
    assert day3.sumprod(EXAMPLE_PAIRS) == EXAMPLE_SUM
    assert day3.sumprod(EXAMPLE_PAIRS_DO_DONT) == EXAMPLE_SUM_DO_DONT


def test_scan_for_muls_do_dont():
    count = 0
    for a, b in zip(day3.scan_for_muls_do_dont(EXAMPLE_INPUT_DO_DONT), EXAMPLE_PAIRS_DO_DONT):
        assert a == b
        count += 1
    assert count == len(EXAMPLE_PAIRS_DO_DONT)


