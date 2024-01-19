import pytest
from day01_trebuchet import isdigit, extract_calib, extract_calib_spelled
from day01_trebuchet import part1, part2


def test_isdigit():
	assert isdigit('0')
	assert isdigit('5')
	assert isdigit('9')
	assert ~isdigit('a')
	assert ~isdigit('\r')
	assert ~isdigit('A')
	assert ~isdigit('@')

def test_calib():
	assert extract_calib('1abc2') == 12
	assert extract_calib('pqr3stu8vwx') == 38
	assert extract_calib('a1b2c3d4e5f') == 15
	assert extract_calib('treb7uchet') == 77

def test_calib_spelled():
	examples = {
		'two1nine': 29,
		'eightwothree': 83,
		'abcone2threexyz': 13,
		'xtwone3four': 24,
		'4nineeightseven2': 42,
		'zoneight234': 14,
		'7pqrstsixteen': 76,
		'qgtwonefive3three': 23,
		'one': 11,
		'five3threeqgtwone': 51,
	}
	for record, value in examples.items():
		assert extract_calib_spelled(record) == value


@pytest.mark.puzzle
def test_day01_part1(benchmark):
	assert benchmark(part1) == 54605


@pytest.mark.puzzle
def test_day01_part2(benchmark):
	assert benchmark(part2) == 55429
