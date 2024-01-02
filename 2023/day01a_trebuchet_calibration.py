fn = 'day01a_trebuchet_calibration_input.txt'


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


if __name__ == '__main__':
	with open(fn, 'r') as f:
		calib_sum = 0
		for line in f:
			calib = extract_calib(line)
			calib_sum += calib

	print(calib_sum)


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
