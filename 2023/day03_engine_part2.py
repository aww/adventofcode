fn = 'day03a_engine_input.txt'


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


def preformat(x: list[str]) -> list[str]:
    out = []
    for s in x:
        out.append(s.replace('\n', '.'))
    return out


if __name__ == '__main__':
    with open(fn, 'r') as f:
        lines = f.readlines()
        lines = preformat(lines)
        pairs = find_gear_pairs(lines)
        print(pairs)
        print(f'Count = {len(pairs)}')
        print(sum([x[0]*x[1] for x in pairs]))  # 507908 too high


def test_find_integer_from():
    assert find_integer_from("....453...", 4) == 453
    assert find_integer_from("....453...", 5) == 453
    assert find_integer_from("....453...", 6) == 453
    assert find_integer_from("....453", 6) == 453
    assert find_integer_from("453......", 0) == 453
    assert find_integer_from("453......", 2) == 453


def test_find_integers_centered():
    assert find_integers_centered("...453.128........", 6) == [453, 128]
    assert find_integers_centered("...453.128........", 5) == [453]
    assert find_integers_centered("...453.128........", 7) == [128]
    assert find_integers_centered("...453.128........", 8) == [128]
    assert find_integers_centered("...453.128........", 9) == [128]
    assert find_integers_centered("...453.128........", 10) == [128]
    assert find_integers_centered("...453.128........", 11) == []


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
    sample_readlines = preformat(sample_readlines)
    pairs = find_gear_pairs(sample_readlines)
    assert ({frozenset([x[0], x[1]]) for x in pairs}
            == {frozenset([467, 35]), frozenset([755, 598])})
