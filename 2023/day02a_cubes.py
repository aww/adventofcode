fn = 'day02a_cubes_input.txt'
pattern = (12, 13, 14)


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


def is_possible(game_records):
	_, results = game_records.split(': ')
	results = list(map(to_rgb, results.split('; ')))
	for r in results:
#		print(r)
		for i in range(3):
			if r[i] > pattern[i]:
				return False
	return True


def game_index(game_record):
	game_label, _ = game_record.split(': ')
	_, idx = game_label.split(' ')
	idx = int(idx)
	return idx


if __name__ == '__main__':
	with open(fn, 'r') as f:
		sum_yes_index = 0
		sum_all_index = 0
		for line in f:
			line = line.strip()
			if is_possible(line):
				sum_yes_index += game_index(line)
#			print(f'DEBUG: {game_index(line)} => {is_possible(line)} for {line.strip()}')
			sum_all_index += game_index(line)
		print(sum_yes_index)  # 2922 too high
#		print(sum_all_index)


def test_rbg():
	assert to_rgb('1 red, 132 green') == [1, 132, 0]
	assert to_rgb("3 blue") == [0, 0, 3]
	assert to_rgb("8 red, 2 green, 1 blue") == [8, 2, 1]

def test_index():
	assert game_index("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 1
	assert game_index("Game 99: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 99

def test_is_possible():
	assert is_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
	assert is_possible("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
	assert ~is_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
	assert ~is_possible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
	assert is_possible("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
	assert ~is_possible("Game 90: 14 blue, 10 red, 2 green; 11 blue, 3 red, 1 green; 5 blue, 2 green, 14 red")
