

PATTERN = (12, 13, 14)


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
#               print(r)
                for i in range(3):
                        if r[i] > PATTERN[i]:
                                return False
        return True


def game_index(game_record):
        game_label, _ = game_record.split(': ')
        _, idx = game_label.split(' ')
        idx = int(idx)
        return idx


def min_possible(game_records):
        _, results = game_records.split(': ')
        results = list(map(to_rgb, results.split('; ')))
        min_possible = [None, None, None]
        for r in results:
                for i in range(3):
                        if min_possible[i] is None or min_possible[i] < r[i]:
                                min_possible[i] = r[i]
        return min_possible


def read_input():
        with open('../private/2023/day02_cubes_input.txt', 'r') as f:
                return f.readlines()


def part1() -> int:
        sum_yes_index = 0
        # sum_all_index = 0
        for line in read_input():
                line = line.strip()
                if is_possible(line):
                        sum_yes_index += game_index(line)
                # print(f'DEBUG: {game_index(line)} => {is_possible(line)} for {line.strip()}')
                # sum_all_index += game_index(line)
        return sum_yes_index  # 2922 too high
        # print(sum_all_index)


def part2() -> int:
        sum_powers = 0
        for line in read_input():
                line = line.strip()
                p = min_possible(line)
                power = p[0] * p[1] * p[2]
                sum_powers += power
        return sum_powers


if __name__ == '__main__':
        print(f"Part 1: {part1()}")
        print(f"Part 2: {part2()}")