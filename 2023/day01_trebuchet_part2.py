import itertools
import re


fn = 'day01a_trebuchet_calibration_input.txt'


NUMBERS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
TO_FIND = []
for k in NUMBERS.keys():
	TO_FIND.append(k)
for v in NUMBERS.values():
	TO_FIND.append(str(v))


def extract_calib_spelled(line):
	first = None
	last = None
	for i in range(len(line)):
		for tf in TO_FIND:
			if line[i:].startswith(tf):
				last = tf
				if first is None:
					first = tf
	try:
		first = NUMBERS[first]
	except KeyError:
		first = int(first)
	try:
		last = NUMBERS[last]
	except KeyError:
		last = int(last)
	calib = first * 10 + last
	print(f'DEBUG: {line.strip()} {first}, ..., {last} => {calib}')
	return calib


if __name__ == '__main__':
	with open(fn, 'r') as f:
		calib_sum = 0
		for line in f:
			calib = extract_calib_spelled(line)
			calib_sum += calib

	print(calib_sum)  # 55427 too low


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
