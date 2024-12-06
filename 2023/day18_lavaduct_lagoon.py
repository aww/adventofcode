from collections import defaultdict


DIRCHAR2INT = {'R': 0, 'D': 1, 'L': 2, 'U': 3}


def read_input(plan: str = None) -> list[tuple[int, int]]:
    if plan is None:
        with open('../private/2023/day18_lavaduct_lagoon_input.txt') as f:
            lines = f.readlines()
    else:
        lines = plan.strip().splitlines()
    result = []
    for line in lines:
        a, b, _ = line.split()
        b = int(b)
        a = DIRCHAR2INT[a]
        # c = c.strip('()')
        result.append((a, b))
    return result


def read_input_fix(plan: str = None) -> list[tuple[int, int]]:
    if plan is None:
        with open('../private/2023/day18_lavaduct_lagoon_input.txt') as f:
            lines = f.readlines()
    else:
        lines = plan.strip().splitlines()
    result = []
    for line in lines:
        _, _, c = line.split()
        c = c.strip('()')
        a = int(c[6:])
        b = int(c[1:6], 16)
        result.append((a, b))
    return result


def is_closed(plan):
    """Is the curve defined in the dig plan closed?"""
    vsum, hsum = 0, 0
    for a, b in plan:
        if a == 0:
            hsum += b
        elif a == 1:
            vsum += b
        elif a == 2:
            hsum -= b
        elif a == 3:
            vsum -= b
        else:
            ValueError(f"Unrecognized direction '{a}' in dig plan")
    return (vsum == 0) and (hsum == 0)


# TURN_DIR = {
#     ('R', 'D'): 1,
#     ('D', 'L'): 1,
#     ('L', 'U'): 1,
#     ('U', 'R'): 1,
#     ('R', 'U'): -1,
#     ('U', 'L'): -1,
#     ('L', 'D'): -1,
#     ('D', 'R'): -1,
# }


def turndir(a, b) -> int:
    td = (a - b) % 4
    assert td == 1 or td == 3
    if td == 3:
        td = -1
    return td


def winding_number(plan):
    """A +1 indicates the boundary circles around clockwise and the interior is on the right side of the boundary
    and -1 indicates the boundary circles around counterclockwise and the interior is on the left side.
    Anything else and this planar curve is not closed or self-intersecting, but +/-1 is not sufficient """
    assert is_closed(plan)
    winding_sum = 0
    for a, b in zip(plan, plan[1:] + [plan[0]]):
        winding_sum += turndir(b[0], a[0])
    assert winding_sum % 4 == 0
    return winding_sum // 4


DIR_MOVE = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1),
}


DIR_INT = {
    0: {1: (0, 1), -1: (0, -1)},
    1: {1: (-1, 0), -1: (1, 0)},
    2: {1: (0, -1), -1: (0, 1)},
    3: {1: (1, 0), -1: (-1, 0)},
}


def normalized_lineset(plan, winding: int = None) -> [set, set, int, int]:
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    x, y = 0, 0
    lineset = set()
    interiorset = set()
    aprevious = ''
    for a, b in plan:
        if winding is not None and aprevious:
            td = turndir(a, aprevious)
            if td * winding < 0:
                # Path turned away from the interior
                # Need to mark points around the corner as interior
                # We use the old delta and deltaint
                add1 = (x + deltaint[0],            y + deltaint[1])
                interiorset.add(add1)
                add2 = (x + deltaint[0] + delta[0], y + deltaint[1] + delta[1])
                interiorset.add(add2)
                pass
        try:
            delta = DIR_MOVE[a]
        except KeyError:
            assert ValueError(f"Unrecognized direction '{a}' in dig plan")
        for i in range(b):
            if winding is not None:
                if winding == 1:
                    deltaint = -delta[1], delta[0]
                elif winding == -1:
                    deltaint = delta[1], -delta[0]
                interiorset.add((x + DIR_INT[a][winding][0],
                                 y + DIR_INT[a][winding][1]))
            x += delta[0]
            y += delta[1]
            lineset.add((x, y))
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y
        aprevious = a
    interiorset -= lineset
    interiorset = {(x-min_x, y - min_y) for x, y in interiorset}
    lineset = {(x-min_x, y - min_y) for x, y in lineset}
    cols, rows = max_x-min_x+1, max_y-min_y+1
    return lineset, interiorset, cols, rows


def draw(cols: int, rows: int, lineset: set, interiorset: set = None) -> str:
    if interiorset is None:
        interiorset = set()
    return '\n'.join(
        [''.join(['#' if (x, y) in lineset else ('O' if (x, y) in interiorset else '.')
                  for x in range(cols)]) for y in range(rows)])


def interior_by_floodfill(lineset, frontier) -> set[tuple[int, int]]:
    interior = set()
    while len(frontier) > 0:
        pt = frontier.pop()
        interior.add(pt)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            pt2 = pt[0] + dx, pt[1] + dy
            if pt2 not in lineset and pt2 not in interior:
                frontier.add(pt2)
    return interior


def normalized_path(plan: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    """The return the x and y coordinate lists  of the endpoints of line segments
    making up the path that the plan specifies."""
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    x, y = 0, 0
    xlist, ylist = [0], [0]
    for a, b in plan:
        try:
            delta = DIR_MOVE[a]
        except KeyError:
            assert ValueError(f"Unrecognized direction '{a}' in dig plan")
        x += delta[0] * b
        y += delta[1] * b
        xlist.append(x)
        ylist.append(y)
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    xlist = list([x1 - min_x for x1 in xlist])
    ylist = list([y1 - min_y for y1 in ylist])
    # cols, rows = max_x-min_x+1, max_y-min_y+1
    return xlist, ylist


def area_by_rasterscan(xlist: list[int], ylist: list[int]) -> int:
    """Slice the region from top to bottom at every point where a vertical line segment begins or ends.
    We can assume the line segments alternate between vertical and horizontal because of how a plan is specified.
    (We asssume there is no backtracking or lines broken into more than on segment.)
    """
    assert len(xlist) == len(ylist)
    xlist.append(xlist[0])
    ylist.append(ylist[0])

    area: int = 0

    # print(f"{xlist=}")
    # print(f"{ylist=}")
    # First collect all the possible corners by y value, sorted.
    # Store lists of the line segments attached to these corners.
    corners = defaultdict(list)
    for x, y1, y2 in zip(xlist, ylist, ylist[1:]):
        if y1 != y2:
            if y1 > y2:  # Reorder the y values so lowest is always first
                y1, y2 = y2, y1
            corners[y1].append((x, y1, y2))
            corners[y2].append((x, y1, y2))
    corners = dict(sorted(corners.items()))
    # print(corners)
    previous_y = None
    # These are segments that pass through the y value of a corner but don't necessarily start or end there.
    continuing_segments = []
    # Now work through all the corners in ascending y value
    #  1. Measure the "area" along these rows which includes enclosed regions
    #    as well as the horizontal segments between corners.
    #  2. Also measure the area in the regions between
    for y in corners.keys():
        if previous_y is not None and previous_y < y - 1:  # This is #2 above
            # print(continuing_segments)
            assert len(continuing_segments) % 2 == 0  # a slice should cross a closed loop an even number of times
            continuing_segments.sort(key=lambda x: x[0])
            # The interior is on only one side of each line, so as we slice horizontally across boundaries
            # The regions between lines alternate between interior and exterior regions.
            in_region = True
            for x1, x2 in zip([x[0] for x in continuing_segments],
                              [x[0] for x in continuing_segments[1:]]):
                if in_region:
                    area += (x2 - x1 + 1) * (y - previous_y - 1)
                    in_region = False
                else:
                    in_region = True
            # print(f"Before {y=} total {area=}")
        previous_y = y

        for seg in corners[y]:
            if seg[2] == y:
                continuing_segments.remove(seg)
        allsegments = sorted(corners[y] + continuing_segments, key=lambda x: x[0])
        for seg in corners[y]:
            if seg[1] == y:
                continuing_segments.append(seg)

        # print(allsegments)  # WW DD UU UDW DUW WUD WUD UDUD DUDU UDDU DUUD
        start_x = -1
        segment_count = 0  # count segments contributing flat walls as 2 but corners (that come paired) as 1
        alternator = 1
        for seg in allsegments:
            if start_x == -1:
                start_x = seg[0]
            is_corner = (y == seg[1] or y == seg[2])
            if is_corner:
                alternator = -alternator
            if y == seg[1]:
                if alternator == 0:
                    alternator = 1
                segment_count += alternator
            elif y == seg[2]:
                if alternator == 0:
                    alternator = -1
                segment_count -= alternator
            else:
                segment_count += 2
            if alternator != 0 and segment_count % 4 == 0:
                area += seg[0] - start_x + 1
                start_x = -1
                segment_count = 0
                alternator = 0

        # for seg1, seg2 in zip(allsegments, allsegments[1:]):  # This is #1 above
        #     w = seg2[0] - seg1[0] + 1
        #     ncorners = (y == seg1[1] or y == seg1[2]) + (y == seg2[1] or y == seg2[2])
        #     total_ncorners += ncorners
        #     if ncorners == 2:  # the final detail I had not accounted for. Corners have to pair up
        #         # and if you have four corners in a row then the region between the middle two is not in the area
        #         # (part of the exterior) but it does indicate a transition between two interior regions.
        #         if total_ncorners % 2 == 0:
        #             area += w
        #         else:
        #             in_region = not in_region
        #     else:
        #         if in_region:
        #             area += w - ncorners
        #         in_region = not in_region
        # print(f"At     {y=} total {area=}")
    return area


SAMPLE_D_CODED = [
    (0, 5),
    (1, 3),
    (2, 1),
    (1, 4),
    (0, 3),
    (3, 2),
    (0, 3),
    (3, 2),
    (2, 3),
    (3, 2),
    (0, 8),
    (1, 3),
    (2, 2),
    (1, 7),
    (2, 3),
    (3, 2),
    (2, 5),
    (1, 3),
    (0, 10),
    (1, 1),
    (2, 13),
    (3, 6),
    (2, 1),
    (3, 6),
    (2, 1),
    (3, 1),
]

def part1() -> int:
    xlist, ylist = normalized_path(SAMPLE_D_CODED)
    assert area_by_rasterscan(xlist, ylist) == 162

    plan = read_input()
    # winding = winding_number(plan)
    # lineset, interiorset, cols, rows = normalized_lineset(plan, winding=winding)
    # # print(interiorset)
    # print(draw(cols, rows, lineset, interiorset))
    # interiorset = interior_by_floodfill(lineset, interiorset)
    # return len(lineset) + len(interiorset)
    xlist, ylist = normalized_path(plan)
    return area_by_rasterscan(xlist, ylist)


def part2() -> int:
    plan = read_input_fix()
    xlist, ylist = normalized_path(plan)
    return area_by_rasterscan(xlist, ylist)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
