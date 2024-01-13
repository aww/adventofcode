import itertools
import cProfile


def read_input(s: str = None) -> list[str]:
    if s is None:
        with open('day14_rolling_rocks_input.txt', 'r') as f:
            return f.readlines()
    return s.splitlines()


def addrock(row, col):
    # assert row[col] == '.'
    return row[:col] + 'O' + row[col+1:]


def removerock(row, col):
    # assert row[col] == 'O'
    return row[:col] + '.' + row[col+1:]


def tilt_north(rocks: list[str]) -> list[str]:
    ncols = len(rocks[0])
    nrows = len(rocks)
    for col in range(ncols):
        startrow = 0
        nrolling = 0
        for row in range(nrows+1):
            if row == nrows or rocks[row][col] == '#':
                if nrolling > 0:
                    # We have some rocks to shift
                    for i in range(startrow, row):
                        if i < startrow + nrolling:
                            rocks[i] = addrock(rocks[i], col)
                        else:
                            rocks[i] = removerock(rocks[i], col)
                nrolling = 0
                startrow = row + 1
            elif rocks[row][col] == 'O':
                nrolling += 1
    return rocks


def rotate(rocks: list[str]) -> list[str]:
    nrows = len(rocks)
    ncols = len(rocks[0])
    result = []
    for inewrow in range(ncols):
        result.append(''.join(rocks[nrows-i-1][inewrow] for i in range(nrows)))
    return result


def spincycle(rocks: list[str]) -> list[str]:
    rocks = tilt_north(rocks)
    rocks = rotate(rocks)
    rocks = tilt_north(rocks)
    rocks = rotate(rocks)
    rocks = tilt_north(rocks)
    rocks = rotate(rocks)
    rocks = tilt_north(rocks)
    rocks = rotate(rocks)
    return rocks


def calc_north_load(rocks: list[str]) -> int:
    nrows = len(rocks)
    load = 0
    for i, row in enumerate(rocks):
        rowvalue = nrows-i
        for c in row:
            if c == 'O':
                load += rowvalue
    return load


def stats(rocks):
    ncols, nrows = len(rocks[0]), len(rocks)
    rolling, fixed = 0, 0
    for i, j in itertools.product(range(nrows), range(ncols)):
        if rocks[i][j] == 'O':
            rolling += 1
        elif rocks[i][j] == '#':
            fixed += 1
    return {'rows': nrows, 'columns': ncols, 'rolling': rolling, 'fixed': fixed}



TEST_SAMPLE_A = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def main():
    rocks = read_input()
    print(stats(rocks))
    rocks = tilt_north(rocks)
    load = calc_north_load(rocks)
    print(f"Load after N tilt: {load}")

    print()
    cache = {}
    rocks = read_input()  # TEST_SAMPLE_A)
    print(stats(rocks))
    ncols = len(rocks[0])
    nrows = len(rocks)
    for icycle in range(201):
        # print(f"Load at {icycle}: {calc_north_load(rocks)}")
        code = ''.join(rocks)
        if code in cache:
            print(f"Cycle {icycle} matches {cache[code]}")
            break
        rocks = spincycle(rocks)
        encoding = 0
        for i, j in itertools.product(range(nrows), range(ncols)):
            if rocks[i][j] == 'O':
                encoding += 2**(i*ncols + j)
        #print(f"{icycle} {encoding}")
    else:
        print(f"Stopping after {icycle} cycles")


if __name__ == '__main__':
    cProfile.run('main()')


TEST_SAMPLE_A_TILTED = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
"""


TEST_SAMPLE_A_CYCLE1 = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
"""


TEST_SAMPLE_A_CYCLE2 = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
"""


TEST_SAMPLE_A_CYCLE3 = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
"""


def test_addrock():
    assert addrock('....OOOO', 2) == '..O.OOOO'
    assert addrock('....OOOO', 0) == 'O...OOOO'
    assert addrock('....OOOO', 7) == '....OOOO'


def test_removerock():
    assert removerock('....OOOO', 7) == '....OOO.'
    assert removerock('....OOOO', 0) == '....OOOO'
    assert removerock('....OOOO', 5) == '....O.OO'


def test_tilt_north():
    assert tilt_north(read_input(TEST_SAMPLE_A)) == read_input(TEST_SAMPLE_A_TILTED)


def test_calc_north_load():
    assert calc_north_load(read_input(TEST_SAMPLE_A_TILTED)) == 136


def test_rotate():
    tst = ["..O.", "#OOO", "..O#", "#..O"]
    tstrot = ["#.#.", "..O.", ".OOO", "O#O."]
    assert rotate(tst) == tstrot


def test_cycle():
    rocks = read_input(TEST_SAMPLE_A)
    cycle1 = spincycle(rocks)
    assert cycle1 == read_input(TEST_SAMPLE_A_CYCLE1)
    cycle2 = spincycle(cycle1)
    assert cycle2 == read_input(TEST_SAMPLE_A_CYCLE2)
    cycle3 = spincycle(cycle2)
    assert cycle3 == read_input(TEST_SAMPLE_A_CYCLE3)

# def test_cycle_find()