import itertools


def read_data(txt: str = None) -> list[str]:
    if txt is None:
        with open('day10_pipes_input.txt', 'r') as f:
            txt = f.read()
    lines = txt.splitlines()
    return lines


CHAR_CONNECTION_CARDINAL = {
    '|': 'NS',
    '-': 'EW',
    'L': 'NE',
    'J': 'NW',
    '7': 'SW',
    'F': 'SE',
}
CARDINAL_TO_VEC = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
}


def negv(v: tuple[int, int]) -> tuple[int, int]:
    return -v[0], -v[1]


def addv(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


CHAR_CONNECTION = {}
for k, v in CHAR_CONNECTION_CARDINAL.items():
    dirs = [CARDINAL_TO_VEC[c] for c in v]
    assert len(dirs) == 2
    CHAR_CONNECTION[k] = {
        negv(dirs[0]): dirs[1],
        negv(dirs[1]): dirs[0],
    }


def find_pipe_loop(field: list[str]) -> list[tuple[int, int]]:
    """Return a list of coordinates for the loop"""
    max_row = len(field)
    max_col = len(field[0])

    def in_range(coord: tuple[int, int]) -> bool:
        return 0 <= coord[0] < max_row and 0 <= coord[0] < max_col

    # Find start
    start_pos = None, None
    for i, j in itertools.product(range(max_row), range(max_col)):
        if field[i][j] == 'S':
            start_pos = i, j
            break

    curr_pos = start_pos
    loop = [start_pos]
    # Find an exit from the start
    for d in CARDINAL_TO_VEC.values():
        candidate_pos = addv(curr_pos, d)
        if (in_range(candidate_pos)
                and (c := field[candidate_pos[0]][candidate_pos[1]]) in CHAR_CONNECTION
                and d in CHAR_CONNECTION[c]):
            print(c)
            curr_pos = candidate_pos
            del candidate_pos
            break
    else:
        raise ValueError(f"Could not find pipe connecting to 'S' at {start_pos}")
    while True:
        if not in_range(curr_pos):
            raise ValueError(f"No connection, pipe flowed out of bounds at {curr_pos}")
        c = field[curr_pos[0]][curr_pos[1]]
        if c == 'S':
            break
        if c in CHAR_CONNECTION:
            flow = CHAR_CONNECTION[c]
            if d in flow:
                loop.append(curr_pos)
                curr_pos = addv(curr_pos, flow[d])
                d = flow[d]
            else:
                print(loop)
                raise ValueError(f"No connection, going {d} into {curr_pos} with '{c}'")
        else:
            print(loop)
            raise ValueError(f"No connection, pipe flowed to '{c}'")
    return loop


def infer_start_flag(loop) -> str:
    # This trick computes directions the loop goes from the start
    # Then it project the four possible directions to the integers 0, 1, 2, 3 with
    # [dir . (1,3) + 3] // 2
    # ( 0, 1) -> 3
    # ( 0,-1) -> 0
    # ( 1, 0) -> 2
    # (-1, 0) -> 1
    dir1 = addv(loop[1], negv(loop[0]))
    prj1 = (dir1[0] + 3*dir1[1] + 3) // 2
    dir2 = addv(loop[-1], negv(loop[0]))
    prj2 = (dir2[0] + 3*dir2[1] + 3) // 2
    # |=2,1  -=3,0   J=1,0   L=1,3   F=2,3   7=0,2
    flag = ' J7-J |L7| F-LF -'[prj1 + 4*prj2]
    return flag


def find_inside_outside(field: list[list[str]], loop: list[tuple[int, int]]) -> list[list[int]]:
    winding = 0
    nrows, ncols = len(field), len(field[0])
    marks = [[0 for _ in range(ncols)] for _ in range(nrows)]
    for i in range(nrows):
        crossing_count = 0
        for j in range(ncols):
            if (i, j) in loop:
                flag = field[i][j]
                # We are going to use some tricks here but the basic idea is to scan across
                # each row and keep track of how often we cross the loop.
                # It is easy for | but for the "corners" we want to count sequences like
                #   L---J or F---7
                # as not crossing but count sequences like
                #   L-*7 or F-*J
                # as crossing. Other patterns should not occur.
                # The start flag is also tricky because we need infer what shape it has.
                #
                # FUTURE IDEA: simplify this with re.sub
                if flag == 'S':
                    # Have to infer what this is
                    flag = infer_start_flag(loop)
                if flag == '|':
                    crossing_count += 2
                elif flag == 'L':   # LJ, F7 = 0   L7, FJ = 1
                    crossing_count += 2
                elif flag == 'J':
                    crossing_count += 2
            else:
                marks[i][j] = (crossing_count % 4) - 1
    return marks


def render(field: list[str], loop: list[tuple[int, int]], infield = None) -> str:
    """Translate the characters in the field to nice terminal graphics unicode characters.
    All the points on the loop are rendered in bold.
    This is not very efficient."""
    new_field = []
    for a in field:
        new_field.append(a)
    for a, b in loop:
        tr_loop = str.maketrans('|-F7LJ', 'i:f1lj')
        new_field[a] = new_field[a][:b] + new_field[a][b].translate(tr_loop) + new_field[a][b+1:]
    for i, row in enumerate(new_field):
        tr_graph = str.maketrans('.|-F7LJi:f1lj', ' │─┌┐└┘┃━┏┓┗┛')
        new_field[i] = row.translate(tr_graph)
    if infield is not None:
        for i, row in enumerate(infield):
            for j, c in enumerate(row):
                if c == 1:
                    new_field[i] = new_field[i][:j] + '█' + new_field[i][j+1:]
    return '\n'.join(new_field)


def main():
    field = read_data()
    loop = find_pipe_loop(field)
    iofield = find_inside_outside(field, loop)
    n_in, n_out, n_loop = 0, 0, 0
    for row in iofield:
        for flag in row:
            if flag == 1:
                n_in += 1
            elif flag == -1:
                n_out += 1
            elif flag == 0:
                n_loop += 1
            else:
                raise ValueError("Invalid in/out value")
    print(render(field, loop, iofield))
    print(f"Loop of size {len(loop)}, half is {len(loop)/2}")
    print(f"In: {n_in}")  # 1313 Too High
    print(f"Out: {n_out}")
    print(f"Loop {n_loop}")
    print(f"Sum: {n_in + n_out + n_loop}")
    print(f"Size: {len(field)} x {len(field[0])} = {len(field)*len(field[0])}")


if __name__ == '__main__':
    main()


TEST_SAMPLE_A = """.....
.S-7.
.|.|.
.L-J.
....."""


TEST_SAMPLE_B = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

TEST_SAMPLE_C = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

TEST_SAMPLE_D = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""


TEST_SAMPLE_E = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


def test_find_pipe_loop():
    pass

def find_inside_for_test(sample):
    field = read_data(sample)
    loop = find_pipe_loop(field)
    iofield = find_inside_outside(field, loop)
    print(render(field, loop, iofield))
    return sum(x == 1 for x in itertools.chain(*iofield))


def test_find_inside():
    assert find_inside_for_test(TEST_SAMPLE_C) == 4
    assert find_inside_for_test(TEST_SAMPLE_D) == 8
    assert find_inside_for_test(TEST_SAMPLE_E) == 10


def test_infer_start_flag():
    assert infer_start_flag([(4,4), (5,4), (3,4)]) == '|'
    assert infer_start_flag([(4,4), (3,4), (5,4)]) == '|'
    assert infer_start_flag([(4,4), (4,3), (4,5)]) == '-'
    assert infer_start_flag([(4,4), (4,5), (4,3)]) == '-'
    assert infer_start_flag([(4,4), (4,3), (5,4)]) == '7'
    assert infer_start_flag([(4,4), (5,4), (4,3)]) == '7'
    assert infer_start_flag([(4,4), (5,4), (4,5)]) == 'F'
    assert infer_start_flag([(4,4), (4,5), (5,4)]) == 'F'
    assert infer_start_flag([(4,4), (3,4), (4,3)]) == 'J'
    assert infer_start_flag([(4,4), (4,3), (3,4)]) == 'J'
