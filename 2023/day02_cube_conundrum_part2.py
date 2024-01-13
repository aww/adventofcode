fn = 'day02a_cubes_input.txt'


def to_rgb(result):
	result = result.strip()
	rgb = [0, 0, 0]
	for color_result in result.split(', '):
		n, color = color_result.split(' ')
		n = int(n)
		if color == 'red':
			rgb[0] = n
		if color == 'green':
			rgb[1] = n
		if color == 'blue':
			rgb[2] = n
	return rgb


def min_possible(game_records):
	_, results = game_records.split(': ')
	results = list(map(to_rgb, results.split('; ')))
	min_possible = [None, None, None]
	for r in results:
		for i in range(3):
			if min_possible[i] is None or min_possible[i] < r[i]:
				min_possible[i] = r[i]
	return min_possible



if __name__ == '__main__':
	with open(fn, 'r') as f:
		sum_powers = 0
		for line in f:
			line = line.strip()
			p = min_possible(line)
			power = p[0] * p[1] * p[2]
			sum_powers += power
		print(sum_powers)


def test_rbg():
	assert to_rgb('1 red, 132 green') == [1, 132, 0]
	assert to_rgb("3 blue") == [0, 0, 3]
	assert to_rgb("8 red, 2 green, 1 blue") == [8, 2, 1]


def test_min_possible():
	assert min_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == [4, 2, 6]
	assert min_possible("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == [1, 3, 4]
	assert min_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == [20, 13, 6]
	assert min_possible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == [14, 3, 15]
	assert min_possible("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == [6, 3, 2]
	assert min_possible("Game 90: 14 blue, 10 red, 2 green; 11 blue, 3 red, 1 green; 5 blue, 2 green, 14 red") == [14, 2, 14]
