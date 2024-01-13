import itertools
import pytest


def read_block(s: str) -> list[str]:
    return s.splitlines()


def read_file() -> list[list[str]]:
    with open('day13_mirrors_input.txt') as f:
        return [read_block(s) for s in f.read().split('\n\n')]


def find_reflection(b: list[str]) -> int:
    ncols = len(b[0])
    nrows = len(b)
    for n in range(1, ncols):
        ncolscheck = min(n, ncols-n)
        for dcol, irow in itertools.product(range(ncolscheck), range(nrows)):
            if b[irow][n-dcol-1] != b[irow][n+dcol]:
                break
        else:
            return n
    for n in range(1, nrows):
        nrowscheck = min(n, nrows-n)
        for drow, icol in itertools.product(range(nrowscheck), range(ncols)):
            if b[n-drow-1][icol] != b[n+drow][icol]:
                break
        else:
            return 100*n
    raise ValueError("No reflection")


def find_reflection_failures(b: list[str]) -> list[tuple[int, int]]:
    """Returns a list of all possible row/col codes and the number of reflection failures."""
    ncols = len(b[0])
    nrows = len(b)
    results = []
    for n in range(1, ncols):
        failures = 0
        ncolscheck = min(n, ncols-n)
        for dcol, irow in itertools.product(range(ncolscheck), range(nrows)):
            if b[irow][n-dcol-1] != b[irow][n+dcol]:
                failures += 1
        results.append((n, failures))
        failures = 0
    for n in range(1, nrows):
        failures = 0
        nrowscheck = min(n, nrows-n)
        for drow, icol in itertools.product(range(nrowscheck), range(ncols)):
            if b[n-drow-1][icol] != b[n+drow][icol]:
                failures += 1
        results.append((n*100, failures))
        failures = 0
    return results


def main():
    blocks = read_file()
    summary = 0
    summary2 = 0
    for b in blocks:
        summary += find_reflection(b)
        failure_counts = find_reflection_failures(b)
        smudges = list(filter(lambda x: x[1] == 1, failure_counts))
        assert len(smudges) == 1
        summary2 += smudges[0][0]
    print(summary)
    print(summary2)


if __name__ == '__main__':
    main()


TEST_SAMPLE_A = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""


TEST_SAMPLE_B = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


@pytest.mark.parametrize('test_input,expected', [(TEST_SAMPLE_A, 5), (TEST_SAMPLE_B, 400)])
def test_find_reflection(test_input, expected):
    assert find_reflection(read_block(test_input)) == expected
