from collections import defaultdict
import itertools


def read_input(s: str = None) -> (dict[list[str]], tuple):
    rows = []
    if s is None:
        with open('../private/2024/day08_resonant_collinearity_input.txt', 'r') as f:
            s = f.read()
    antennas = defaultdict(list)
    linesizes = []
    for i, line in enumerate(s.strip().splitlines()):
        line = line.strip()
        if len(line) > 0:
            linesizes.append(len(line))
            for j, sym in enumerate(line):
                if sym != '.':
                    antennas[sym].append((j,i))
    assert min(linesizes) == max(linesizes)
    gridsize = (linesizes[0], len(linesizes))
    return antennas, gridsize


def find_nodes(ant, gridsize) -> list:
    nodelocs = set()
    for sym, antlocs in ant.items():
        for a, b in itertools.combinations(antlocs, 2):
            #  Example: a=(6,5) b=(8,8)
            cand1 = 2*a[0]-b[0], 2*a[1]-b[1]  # (4,2)
            cand2 = 2*b[0]-a[0], 2*b[1]-a[1]  # (10,11)
            if 0 <= cand1[0] < gridsize[0] and 0 <= cand1[1] < gridsize[1]:
                nodelocs.add(cand1)
            if 0 <= cand2[0] < gridsize[0] and 0 <= cand2[1] < gridsize[1]:
                nodelocs.add(cand2)
    return nodelocs


def find_nodes_res(ant, gridsize) -> list:
    nodelocs = set()
    for sym, antlocs in ant.items():
        for a, b in itertools.combinations(antlocs, 2):
            delta = a[0]-b[0], a[1]-b[1]
            p = a
            while(True):
                if 0 <= p[0] < gridsize[0] and 0 <= p[1] < gridsize[1]:
                    nodelocs.add(p)
                else:
                    break
                p = p[0] + delta[0], p[1] + delta[1]
            p = b
            while(True):
                if 0 <= p[0] < gridsize[0] and 0 <= p[1] < gridsize[1]:
                    nodelocs.add(p)
                else:
                    break
                p = p[0] - delta[0], p[1] - delta[1]
    return nodelocs


def part1() -> int:
    antennas, gridsize = read_input()
    locs = find_nodes(antennas, gridsize)
    return len(locs)


def part2() -> int:
    antennas, gridsize = read_input()
    locs = find_nodes_res(antennas, gridsize)
    return len(locs)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
