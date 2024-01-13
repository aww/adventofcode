from collections.abc import Callable


def read_input():
    with open('../private/2023/day03_engine_input.txt', 'r') as f:
        return f.readlines()


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


def find_integer_from(x, col: int) -> int:
    """Find the integer that intersects x[col]
    This will raise an exception if x[col] is not a digit."""
    # Find the first character of the integer
    col_start = None
    for i in range(col+1):
        if x[col-i].isdigit():
            col_start = col-i
        else:
            break

    num = 0
    for i in range(col_start, len(x)):
        if x[i].isdigit():
            num = 10*num + int(x[i])
        else:
            break
    return num


def find_integers_centered(x: str, col: int) -> list[int]:
    """Find one or two integers that intersect the three characters centered at col
    Return results as a string"""
    if x[col].isdigit():
        return [find_integer_from(x, col)]
    integers = []
    if col > 0 and x[col-1].isdigit():
        integers.append(find_integer_from(x, col-1))
    if col < len(x)-1 and x[col+1].isdigit():
        integers.append(find_integer_from(x, col+1))
    return integers


def find_integers_around(a: list[str], x1: int, y1: int):
    integers: list[int] = []
    # Scan above
    if y1 > 0:
        integers.extend(find_integers_centered(a[y1-1], x1))
    # Scan below
    if y1 < len(a)-1:
        integers.extend(find_integers_centered(a[y1+1], x1))
    # Scan left
    if x1 > 0 and a[y1][x1-1].isdigit():
        integers.append(find_integer_from(a[y1], x1-1))
    # Scan right
    if x1 < len(a[y1])-1 and a[y1][x1+1].isdigit():
        integers.append(find_integer_from(a[y1], x1+1))
    return integers


def find_gear_pairs(x: list[str]):
    pairs: list[tuple[int, int, int, int]] = []
    for row in range(len(x)):
        row_str = x[row]
        for col in range(len(row_str)):
            c = row_str[col]
            if c == '*':
                integers = find_integers_around(x, col, row)
                if len(integers) == 2:
                    pairs.append((integers[0], integers[1], col, row))
    return pairs


def main():
    lines = preformat(read_input())
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

    lines = preformat(read_input())
    pairs = find_gear_pairs(lines)
    print(pairs)
    print(f'Count = {len(pairs)}')
    print(sum([x[0]*x[1] for x in pairs]))  # 507908 too high


if __name__ == '__main__':
    main()
