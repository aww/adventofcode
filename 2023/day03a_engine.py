from collections.abc import Callable

fn = 'day03a_engine_input.txt'


def search_around_for(a: list[str],
                      x1: int, y1: int, x2: int, y2: int,
                      is_a: Callable[[str], bool]):
    assert x1 <= x2
    assert y1 <= y2
    xmax = len(a[0]) - 1
    ymax = len(a) - 1
    # Scan above and below
    for j in range(max(x1-1, 0), min(x2+1, xmax) + 1):
        if y1 > 0 and is_a(a[y1 - 1][j]):
            return True
        if y2 < ymax and is_a(a[y2 + 1][j]):
            return True
    # Scan left and right
    for i in range(max(y1-1, 0), min(y2+1, ymax) + 1):
        if x1 > 0 and is_a(a[i][x1 - 1]):
            return True
        if x2 < xmax and is_a(a[i][x2 + 1]):
            return True
    return False


def find_adjacent_numbers(x: list[str]):
    num_col = None
    num_str: str = ''
    yes: list[tuple[int, int, int]] = []
    no: list[tuple[int, int, int]] = []
    for row in range(len(x)):
        row_str = x[row]
        for col in range(len(row_str)):
            c = row_str[col]
            if c.isdigit():
                if num_col is None:
                    # start of number
                    num_col = col
                    num_str = c
                else:
                    # rest of number
                    num_str += c
            else:
                if num_col is not None:
                    # start of gap - search around
                    width = len(num_str)
                    accept = search_around_for(x, col-width, row, col-1, row, is_symbol)
                    if accept:
                        yes.append((int(num_str), col-width, row))
                    else:
                        no.append((int(num_str), col-width, row))
                    num_col = None
                    num_str = ''
    return yes, no


def find_numbers(x: list[str]):
    num_list = []
    num = 0
    for line in x:
        for c in line:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if num > 0:
                    num_list.append(num)
                    num = 0
    return num_list


def is_symbol(c: str):
    return c != '.' and ~c.isdigit()

def preformat(x: list[str]) -> list[str]:
    out = []
    for l in x:
        out.append(l.replace('\n', '.'))
    return out


if __name__ == '__main__':
    with open(fn, 'r') as f:
        lines = f.readlines()
        lines = preformat(lines)
        nums = find_numbers(lines)
        print(f'{len(nums)} found')
        accepted, not_accepted = find_adjacent_numbers(lines)
        print(accepted)
        print(f'Count = {len(accepted)}')
        print(sum([x[0] for x in accepted]))  # 507908 too high
        print(not_accepted)
        print(f'Count = {len(not_accepted)}')
        print(sum([x[0] for x in not_accepted]))
        # append(f.readline())
        # lines.append(f.readline())
        # lines.append(f.readline())
        # # Do stuff
        #
        # lines = f.readlines()
        #


def test_find_adjacent_numbers():
    sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    # This simulates file.readlines()
    sample_readlines = sample.splitlines(keepends=True)
    sample_readlines = preformat(readlines)
    yes, no = find_adjacent_numbers(sample_readlines)
    assert set([x[0] for x in yes]) == {467, 35, 633, 617, 592, 755, 664, 598}
    assert set([x[0] for x in no]) == {114, 58}
