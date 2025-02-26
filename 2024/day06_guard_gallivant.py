from collections import defaultdict
import copy
import bisect
from typing import Tuple


def read_input(s: str = None) -> list[str]:
    rows = []
    if s is None:
        with open('../private/2024/day06_guard_gallivant_input.txt', 'r') as f:
            s = f.read()
    obstacles = []
    start = None
    linesizes = []
    for j, line in enumerate(s.strip().splitlines()):
        line = line.strip()
        linesizes.append(len(line))
        for i, c in enumerate(line):
            if c == '#':
                obstacles.append((i,j))
            elif c == '^':
                start = (i,j)
    assert min(linesizes) == max(linesizes)
    gridsize = (linesizes[0], len(linesizes))
    return gridsize, start, obstacles


# def visit_count_of_trip(gridsize, start, obstacles) -> int:
#     """Find the number of cells visited from start to leaving the region, turning at each obstacle"""
#     #
#     # The basic scheme is find the nearest blocker in the current direction by, for instance,
#     # finding the max y-value of the y-values of blockers on the current x and below the current y
#     # 1. Check for no blockers and if so use the extremity
#     # 2. Add the intervening coordinates into a visited set
#     # 3. Update the position
#     #
#     v, h = defaultdict(list), defaultdict(list)
#     for a,b in obstacles:
#         # Create some mapping between a horizontal or vertical position and all the
#         # obstacles on that slice.
#         v[a].append(b)
#         h[b].append(a)
#     #
#     # Initially I made the mistake of thinking I needed to count the number of steps
#     # (though counting a 2-cell path as 2 steps, which may not be exactly what one might mean).
#     # As far as I know that worked correctly but what the question was actually asking for
#     # the number of positions visited, which is less because of overlaps.
#     # I'm keeing the step code around, just commented out.
#     #
#     #steps = 1
#     dir = 0  # 0=up, 1=right, 2=down, 3=left
#     pos = start
#     visited = set()
#     visited.add(start)
#     while(True):
#         if dir == 0:
#             try:
#                 yobs = max([y for y in v[pos[0]] if y < pos[1]])
#             except (ValueError, KeyError):
#                 visited.update([(pos[0], y) for y in range(0, pos[1])])
#                 #steps += pos[1]
#                 break
#             visited.update([(pos[0], y) for y in range(yobs + 1, pos[1])])
#             #steps += pos[1] - yobs - 1
#             pos = (pos[0], yobs + 1)
#         elif dir == 1:
#             try:
#                 xobs = min([x for x in h[pos[1]] if x > pos[0]])
#             except (ValueError, KeyError):
#                 visited.update([(x, pos[1]) for x in range(pos[0] + 1, gridsize[0])])
#                 #steps += gridsize[0] - pos[0]
#                 break
#             visited.update([(x, pos[1]) for x in range(pos[0] + 1, xobs)])
#             #steps += xobs - pos[0] - 1
#             pos = (xobs - 1, pos[1])
#         elif dir == 2:
#             try:
#                 yobs = min([y for y in v[pos[0]] if y > pos[1]])
#             except (ValueError, KeyError):
#                 visited.update([(pos[0], y) for y in range(pos[1] + 1, gridsize[1])])
#                 #steps += gridsize[1] - pos[1]
#                 break
#             visited.update([(pos[0], y) for y in range(pos[1] + 1, yobs)])
#             #steps += yobs - pos[1] - 1
#             pos = (pos[0], yobs - 1)
#         elif dir == 3:
#             try:
#                 xobs = max([x for x in h[pos[1]] if x < pos[0]])
#             except (ValueError, KeyError):
#                 visited.update([(x, pos[1]) for x in range(0, pos[0])])
#                 #steps += pos[0]
#                 break
#             visited.update([(x, pos[1]) for x in range(xobs + 1, pos[0])])
#             #steps += pos[0] - xobs - 1
#             pos = (xobs + 1, pos[1])
#         dir = (dir + 1) % 4
#     return len(visited)


class Obstacles():
    def __init__(self, obstacles):
        self.o = obstacles
        self.slice = defaultdict(list), defaultdict(list)  # i=0 vertical slice, i=1 horizontal
        for a,b in obstacles:
            # Create some mapping between a horizontal or vertical position and all the
            # obstacles on that slice.
            self.slice[0][a].append(b)
            self.slice[1][b].append(a)
        for i in range(2):
            for x in self.slice[i].keys():
                self.slice[i][x].sort()

    def next(self, pos, d):
        assert d[0] == 0 or d[1] == 0
        assert abs(sum(d)) == 1
        i = 0 if d[1] else 1
        next_obs = list(pos)
        if pos[i] in self.slice[i]:
            slc = self.slice[i][pos[i]]
            bi = bisect.bisect_left(slc, pos[1-i])
            if d[1-i] > 0:
                if bi >= len(slc):
                    return None
                else:
                    next_obs[1-i] = slc[bi]
            else:
                if bi == 0:
                    return None
                else:
                    next_obs[1-i] = slc[bi-1]
            return tuple(next_obs)
        #     try:
        #     if d[1]:
        #         if sum(d) < 0:
        #             yobs = max([y for y in self.v[pos[0]] if y < pos[1]])
        #         else:
        #             yobs = min([y for y in self.v[pos[0]] if y > pos[1]])
        #     else:
        #         if sum(d) < 0:
        #             xobs = max([x for x in self.h[pos[1]] if x < pos[0]])
        #         else:
        #             xobs = min([x for x in self.h[pos[1]] if x > pos[0]])
        # except (ValueError, KeyError):
        #     return None
        # return xobs, yobs


def rotdir(d):
    "(0,-1) -> (1,0) -> (0,1) -> (-1,0) -> (0,-1)"
    return -d[1], d[0]


# def adddir(pos, d):
#     return pos[0]+d[0], pos[1]+d[1]


# def eqv(v1, v2):
#     return v1[0] == v2[0] and v1[1] == v2[1]


# def ingrid(pos, gridsize):
#     return pos[0] >= 0 and pos[1] >= 0 and pos[0] < gridsize[0] and pos[1] < gridsize[1]


def trip(gridsize, start, obstacles) -> Tuple[list, bool]:
    obs = Obstacles(obstacles)
    pos = start
    d = (0,-1)
    #steps = 0
    vertices = [start]
    # The following is only used for checking for cycles, deliberately not including start.
    # Start could be revisited and not be part of a cycle:
    # consider the case of an obstacle behind the start point.
    vertexset = set()
    while(True):
        nxtobs = obs.next(pos, d)
        if nxtobs is None:
            match d:
                case (0,1):
                    pos = (pos[0], gridsize[1] - 1)
                    #segmentsteps += gridsize[1] - pos[1]
                case (0,-1):
                    pos = (pos[0], 0)
                    #segmentsteps += pos[1] + 1
                case (1,0):
                    pos = (gridsize[0] - 1, pos[1])
                    #segmentsteps += gridsize[0] - pos[0]
                case (-1,0):
                    pos = (0, pos[1])
                    #segmentsteps += pos[0] + 1
            # print(f"{len(vertices)} {segmentsteps=}")
            #steps += segmentsteps
            vertices.append(pos)
            return vertices, False
        #segmentsteps = abs(pos[0]-nxtobs[0]) + abs(pos[1]-nxtobs[1]) - 1
        # print(f"{len(vertices)} {segmentsteps=}")
        #steps += segmentsteps
        pos = nxtobs[0]-d[0], nxtobs[1]-d[1]  # next position is a step back from next obstacle
        if pos != vertices[-1]:  # two obstacles diagonal from each other can cause rotation in place
            vertices.append(pos)
            if pos in vertexset:
                return vertices, True  # In a cycle
            vertexset.add(pos)
        d = rotdir(d)


def tripcoverage(vertices) -> int:
    coverage = set()
    prv = vertices[0]
    for nxt in vertices[1:]:
        if prv[0] < nxt[0]:
            for x in range(prv[0], nxt[0]):
                coverage.add((x, prv[1]))
        elif prv[0] > nxt[0]:
            for x in range(prv[0], nxt[0], -1):
                coverage.add((x, prv[1]))
        elif prv[1] < nxt[1]:
            for y in range(prv[1], nxt[1]):
                coverage.add((prv[0], y))
        elif prv[1] > nxt[1]:
            for y in range(prv[1], nxt[1], -1):
                coverage.add((prv[0], y))
        else:
            assert ValueError(f"Vertices do not differ: {prv}, {nxt}")
        prv = nxt
    coverage.add(vertices[-1])
    return coverage


def tripdistance(vertices) -> int:
    distance = 1
    prv = vertices[0]
    for nxt in vertices[1:]:
        distance += abs(nxt[0]-prv[0]) + abs(nxt[1]-prv[1])
        prv = nxt
    return distance


def visit_count_of_trip(gridsize, start, obstacles) -> int:
    vertices, isloop = trip(gridsize, start, obstacles)
    if isloop:
        assert ValueError("Found a loop in problem")
    coverage = len(tripcoverage(vertices))
    return coverage


def possible_loop_obstacles(gridsize, start, obstacles) -> int:
    vertices, isloop = trip(gridsize, start, obstacles)
    if isloop:
        assert ValueError("Found a loop in problem")
    coverage = tripcoverage(vertices)
    coverage.remove(start)
    loopobs = set()
    loopobsvert = []
    for p in coverage:
        vertices, isloop = trip(gridsize, start, obstacles + [p]) 
        if isloop:
            loopobs.add(p)
            loopobsvert.append((p, vertices))
    # for p, v in loopobsvert:
    #     print(f"{p} -> {v}")
    return loopobs


def possible_loop_count(gridsize, start, obstacles) -> int:
    loopobs = possible_loop_obstacles(gridsize, start, obstacles)
    return len(loopobs)


def part1() -> int:
    gridsize, start, obstacles = read_input()
    return visit_count_of_trip(gridsize, start, obstacles)


def part2() -> int:
    gridsize, start, obstacles = read_input()
    return possible_loop_count(gridsize, start, obstacles)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
