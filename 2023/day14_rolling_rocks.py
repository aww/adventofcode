import numpy as np
# from typing import TypeAlias
# Grid = TypeAlias('Grid', np.ndarray[np.uint8])


def read_input(s: str = None) -> np.ndarray[np.uint8]:
    if s is None:
        with open('day14_rolling_rocks_input.txt', 'r') as f:
            lines = f.read().strip().splitlines()
    else:
        lines = s.strip().splitlines()
    nrows, ncols = len(lines), len(lines[0])
    rocks = np.zeros((nrows, ncols), dtype=np.uint8)
    for irow, l in enumerate(lines):
        for icol, c in enumerate(l):
            if c == 'O':
                rocks[irow, icol] = 1
            elif c == '#':
                rocks[irow, icol] = 2
            elif c != '.':
                raise ValueError(f"Unrecognized character: '{c}'")
    return rocks


def prettyprint(a: np.ndarray[np.uint8]):
    for i in range(a.shape[1]):
        print(''.join(map(lambda x: {0:'.', 1:'O', 2:'#'}[x], a[i,])))


def stats(rocks: np.ndarray[np.uint8]):
    rolling, fixed = np.sum(rocks == 1), np.sum(rocks == 2)
    load = calc_north_load(rocks)
    return {
        'rows': rocks.shape[0], 'columns': rocks.shape[1],
        'rolling': rolling, 'fixed': fixed,
        'load': load,
    }


def tilt_north(rocks: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    """We simulate rolling all the round rocks (1) north (negative first-axis direction)
    until they settle against the edge, a fixed rock (2), or other round rocks.

    The algorithm I use is to iterate from the north counting rolling rocks until hitting
    a fixed rock or the edge. Then I fill the rocks I counted against the previous fixed edge to the north.
    This involves one iteration over the grid and an for each round rock.
    So basically proportional to the size of the grid.
    """
    nrows, ncols = rocks.shape
    for icol in range(ncols):
        startrow = 0
        nrolling = 0
        for irow in range(nrows+1):
            if irow == nrows or rocks[irow, icol] == 2:
                if nrolling > 0:
                    # We have some rocks to shift
                    for i in range(startrow, irow):
                        if i < startrow + nrolling:
                            rocks[i, icol] = 1
                nrolling = 0
                startrow = irow + 1
            elif rocks[irow, icol] == 1:
                rocks[irow, icol] = 0
                nrolling += 1
    return rocks


def calc_north_load(rocks: np.ndarray[np.uint8]) -> int:
    return np.sum(np.sum(rocks == 1, axis=1) * range(rocks.shape[0], 0, -1))


def rot(rocks: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    """Rotate the grid clockwise."""
    return np.rot90(rocks, k=-1)


def rotcounter(rocks: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    """Rotate the grid counterclockwise."""
    return np.rot90(rocks, k=1)


def spincycle(rocks: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    tilt_north(rocks)
    rocks = rot(rocks)
    tilt_north(rocks)
    rocks = rot(rocks)
    tilt_north(rocks)
    rocks = rot(rocks)
    tilt_north(rocks)
    rocks = rot(rocks)
    return rocks


def applyspincycles(rocks, n=1, verbose=False):
    """Apply n spin cycles to rocks. Optimized by looking for a cycle and then using this information to skip ahead."""
    cyclecache = {}
    icycle = 0
    findingcycle = True
    while icycle < n:
        if findingcycle and (encoding := rocks.tobytes()) in cyclecache:
            cyclelength = icycle - cyclecache[encoding]
            ncyclesskipped = (n - icycle) // cyclelength
            icycle += cyclelength * ncyclesskipped
            if verbose:
                print(f"Cycle #{icycle} matches cycle #{cyclecache[encoding]}, cycling with period {cyclelength}")
                print(f"Skipping {ncyclesskipped} cycles to cycle #{icycle}")
            findingcycle = False
        else:
            cyclecache[encoding] = icycle
        rocks = spincycle(rocks)
        icycle += 1
    if verbose:
        print(f"Completed {icycle} spin cycles")
    return rocks


def main():
    print("Part 1")
    print("===================")
    rocks = read_input()
    print(f"Initial: {stats(rocks)}")
    tilt_north(rocks)
    print(f"After a shift north: {stats(rocks)}")

    print()
    print("Part 2")
    print("===================")
    rocks = read_input()
    rocks = applyspincycles(rocks, n=1000000000, verbose=True)
    print(stats(rocks))


if __name__ == '__main__':
    main()


TEST_SAMPLE_A = """
O....#....
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


TEST_SAMPLE_A_TILTED = """
OOOO.#.O..
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


TEST_SAMPLE_A_CYCLE1 = """
.....#....
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


TEST_SAMPLE_A_CYCLE2 = """
.....#....
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


TEST_SAMPLE_A_CYCLE3 = """
.....#....
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


def test_tilt_north():
    assert (tilt_north(read_input(TEST_SAMPLE_A)) == read_input(TEST_SAMPLE_A_TILTED)).all()


def test_rotate():
    tst = np.array([[0, 0, 1, 0], [2, 1, 1, 1], [0, 0, 1, 2], [2, 0, 0, 1]])
    tstrot = np.array([[2, 0, 2, 0], [0, 0, 1, 0], [0, 1, 1, 1], [1, 2, 1, 0]])
    assert (rot(tst) == tstrot).all()


def test_calc_north_load():
    assert calc_north_load(read_input(TEST_SAMPLE_A_TILTED)) == 136


def test_cycle():
    rocks = read_input(TEST_SAMPLE_A)
    cycle1 = spincycle(rocks)
    assert (cycle1 == read_input(TEST_SAMPLE_A_CYCLE1)).all()
    cycle2 = spincycle(cycle1)
    assert (cycle2 == read_input(TEST_SAMPLE_A_CYCLE2)).all()
    cycle3 = spincycle(cycle2)
    assert (cycle3 == read_input(TEST_SAMPLE_A_CYCLE3)).all()


def test_applyspincycles():
    rocks = read_input(TEST_SAMPLE_A)
    rocks = applyspincycles(rocks, n=1000000000)
    assert stats(rocks)['load'] == 64
