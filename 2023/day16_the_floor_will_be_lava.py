import numpy as np


MAP = {
    '.': 0,
    '\\': 1,
    '/': 2,
    '-': 3,
    '|': 4,
}


MAPBACK = ['.', '\\', '/', '-', '|']


INOUTMAP = {
    0: {'right': ['right'], 'left': ['left'], 'up': ['up'], 'down': ['down']},
    1: {'right': ['down'], 'left': ['up'], 'up': ['left'], 'down': ['right']},
    2: {'right': ['up'], 'left': ['down'], 'up': ['right'], 'down': ['left']},
    3: {'right': ['right'], 'left': ['left'], 'up': ['left', 'right'], 'down': ['left', 'right']},
    4: {'right': ['up', 'down'], 'left': ['up', 'down'], 'up': ['up'], 'down': ['down']},
}

OFFSETMAP = {
    'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0),
}


def read_input(s: str = None) -> np.ndarray:
    if s is None:
        with open('../private/2023/day16_beams_input.txt', 'r') as f:
            lines = f.read().strip().splitlines()
    else:
        lines = s.strip().splitlines()
    return np.array([[MAP[y] for y in x] for x in lines], dtype=np.uint8)


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def trace(grid: np.ndarray, start=((0, 0), 'right')) -> np.ndarray:
    donebefore = set()
    energized = np.zeros_like(grid)
    beams = [start]
    while beams:
        b = beams.pop()
        if b in donebefore:
            continue
        donebefore.add(b)
        pos, d = b
        if min(pos) < 0 or pos[0] >= grid.shape[0] or pos[1] >= grid.shape[1]:
            continue  # left the grid
        energized[pos] = 1
        for outdir in INOUTMAP[grid[pos]][d]:
            beams.append((add(pos, OFFSETMAP[outdir]), outdir))
    return energized


def traceall(grid: np.ndarray) -> int:
    e = []
    for i in range(grid.shape[1]):
        e.append(np.sum(trace(grid, start=((0, i), 'down'))))
        e.append(np.sum(trace(grid, start=((grid.shape[0]-1, i), 'up'))))
    for i in range(grid.shape[0]):
        e.append(np.sum(trace(grid, start=((i, 0), 'right'))))
        e.append(np.sum(trace(grid, start=((i, grid.shape[1]-1), 'left'))))
    return max(e)


def main():
    print("Part 1")
    print("===================")
    grid = read_input()
    energized = trace(grid)
    print(f"Total energized cells: {np.sum(energized)}")
    print()
    print("Part 2")
    print("===================")
    grid = read_input()
    maxenergized = traceall(grid)
    print(f"Max energized cells: {maxenergized}")


if __name__ == '__main__':
    main()
