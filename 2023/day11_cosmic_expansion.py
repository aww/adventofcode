import itertools
import pytest


def read_data(txt: str = None) -> list[tuple[int, int]]:
    result = []
    if txt is None:
        with open('day11_galaxy_input.txt', 'r') as f:
            for row, line in enumerate(f.readlines()):
                for col, c in enumerate(line):
                    if c == '#':
                        result.append((row, col))
    else:
        for row, line in enumerate(txt.splitlines()):
            for col, c in enumerate(line):
                if c == '#':
                    result.append((row, col))
    return result


def galaxy_expand(g: list[tuple[int, int]], expansionfactor=2) -> list[tuple[int, int]]:
    rows = set(row for row, _ in g)
    cols = set(col for _, col in g)
    expand_row = sorted(set(range(max(rows))) - rows)
    expand_col = sorted(set(range(max(cols))) - cols)
    print(expand_row)
    print(expand_col)
    newg = []
    for x in g:
        row_shift, col_shift = 0, 0
        for row in expand_row:
            if row < x[0]:
                row_shift += expansionfactor-1
            # else:
            #     break
        for col in expand_col:
            if col < x[1]:
                col_shift += expansionfactor-1
            # else:
            #     break
        newg.append((x[0]+row_shift, x[1]+col_shift))
    return newg


def galaxy_find_shortest_paths(g: list[tuple[int, int]]) -> list[int]:
    lengths = []
    for a, b in itertools.combinations(g, 2):
        lengths.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))
    return lengths


def main():
    g = read_data()
    g = galaxy_expand(g)
    paths = galaxy_find_shortest_paths(g)
    print(f"Number of paths: {len(paths)}")
    print(f"Total length: {sum(paths)}")
    print("Part2")
    g = read_data()
    g = galaxy_expand(g, expansionfactor=1000000)
    paths = galaxy_find_shortest_paths(g)
    print(f"Number of paths: {len(paths)}")
    print(f"Total length: {sum(paths)}")  # too high: 553224968560


if __name__ == '__main__':
    main()


TEST_SAMPLE_A = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_read_data():
    g = read_data(TEST_SAMPLE_A)
    answer = [(0, 3), (1, 7), (2, 0), (4, 6), (5, 1), (6, 9), (8, 7), (9, 0), (9, 4)]
    assert set(g) == set(answer)


def test_galaxy_expand():
    g = read_data(TEST_SAMPLE_A)
    g = galaxy_expand(g)
    answer = [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]
    assert set(g) == set(answer)


@pytest.mark.parametrize(
    "expansionfactor,answer",
    [(2, 374), (10, 1030), (100, 8410)]
)
def test_galaxy_distances(expansionfactor, answer):
    g = read_data(TEST_SAMPLE_A)
    g = galaxy_expand(g, expansionfactor=expansionfactor)
    assert sum(galaxy_find_shortest_paths(g)) == answer
