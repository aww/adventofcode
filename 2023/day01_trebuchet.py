import itertools
import re


def read_input():
        with open('../private/2023/day01_trebuchet_calibration_input.txt', 'r') as f:
                return f.readlines()


def isdigit(c):
	return ord('0') <= ord(c) and ord(c) <= ord('9')


def extract_calib(line):
	first = None
	last = None
	for c in line.strip():
		if isdigit(c):
			if first is None:
				first = int(c)
			last = int(c)
	calib = first * 10 + last
	return calib


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
	# print(f'DEBUG: {line.strip()} {first}, ..., {last} => {calib}')
	return calib


def main():
	calib_sum = sum(extract_calib_spelled(line) for line in read_input())
	print(calib_sum)  # 55427 too low

	calib_sum = sum(extract_calib(line) for line in read_input())
	print(calib_sum)


if __name__ == '__main__':
        main()
