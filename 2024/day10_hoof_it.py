from collections import defaultdict
from collections.abc import Generator


Position = tuple[int, int]
Grid = list[list[int]]
Network = dict[Position, list[Position]]


def read_input(s: str | None = None) -> Grid:
    rows = []
    if s is None:
        with open("../private/2024/day10_hoof_it_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            rows.append(list(map(int, line)))
    rowlengths = list(len(x) for x in rows)
    assert min(rowlengths) == max(rowlengths)
    return rows


def findends(p: Position, net: Network) -> Generator[Position, None, None]:
    if p not in net:
        yield p
    else:
        for nextp in net[p]:
            yield from findends(nextp, net)


def stepupdownnetwork(a: Grid) -> tuple[Network, Network]:
    stepupnetwork: Network = dict()
    stepdownnetwork: Network = dict()
    nrows, ncols = len(a), len(a[0])
    for i in range(nrows):
        for j in range(ncols):
            height: int = a[i][j]
            stepups: list[Position] = []
            stepdowns: list[Position] = []
            if i > 0:
                if a[i - 1][j] == height + 1:
                    stepups.append((i - 1, j))
                if a[i - 1][j] == height - 1:
                    stepdowns.append((i - 1, j))
            if j > 0:
                if a[i][j - 1] == height + 1:
                    stepups.append((i, j - 1))
                if a[i][j - 1] == height - 1:
                    stepdowns.append((i, j - 1))
            if i < nrows - 1:
                if a[i + 1][j] == height + 1:
                    stepups.append((i + 1, j))
                if a[i + 1][j] == height - 1:
                    stepdowns.append((i + 1, j))
            if j < ncols - 1:
                if a[i][j + 1] == height + 1:
                    stepups.append((i, j + 1))
                if a[i][j + 1] == height - 1:
                    stepdowns.append((i, j + 1))
            if len(stepups) > 0:
                stepupnetwork[(i, j)] = stepups
            if len(stepdowns) > 0:
                stepdownnetwork[(i, j)] = stepdowns
    return stepupnetwork, stepdownnetwork


def valuemap(a: Grid) -> dict[int, list[Position]]:
    result = defaultdict(list)
    nrows, ncols = len(a), len(a[0])
    for i in range(nrows):
        for j in range(ncols):
            result[a[i][j]].append((i, j))
    return result


def countroutes(frm: Position, to: list[Position], net: Network) -> int:
    if frm in to:
        return 1
    if frm in net:
        nroutes = 0
        for nxt in net[frm]:
            nroutes += countroutes(nxt, to, net)
        return nroutes
    return 0


def trailheadratingsum(a: Grid) -> int:
    stepupnetwork, _ = stepupdownnetwork(a)
    vmap = valuemap(a)
    ratingsum = 0
    for z in vmap[0]:
        ratingsum += countroutes(z, vmap[9], stepupnetwork)
    return ratingsum


def trailheadscoresum(a: Grid) -> int:
    stepupnetwork, _ = stepupdownnetwork(a)
    vmap = valuemap(a)
    zeros: list[Position] = vmap[0]
    scoresum = 0
    for z in zeros:
        fulltrailend = set()
        for end in findends(z, stepupnetwork):
            if a[end[0]][end[1]] == 9:
                fulltrailend.add(end)
        score = len(fulltrailend)
        scoresum += score
    return scoresum


def part1() -> int:
    input = read_input()
    score = trailheadscoresum(input)
    return score


def part2() -> int:
    input = read_input()
    rating = trailheadratingsum(input)
    return rating


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
