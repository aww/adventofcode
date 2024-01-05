def read_data(txt: str = None) -> list[list[int]]:
    if txt is None:
        with open('day09_oasis_input.txt', 'r') as f:
            txt = f.read()
    lines = txt.splitlines()
    result = []
    for x in lines:
        result.append(list(map(int, x.split())))
    return result


def extrapolate_values(data: list[int], previous=False) -> int:
    if all(d == 0 for d in data):
        return 0
    differences = [b-a for a, b in zip(data, data[1:])]
    extrap = extrapolate_values(differences, previous)
    if previous:
        return data[0] - extrap
    else:
        return data[-1] + extrap


def extrapolate_values_for_all(data: list[list[int]], previous=False) -> list[int]:
    return [extrapolate_values(d, previous) for d in data]


def main():
    data = read_data()
    values = extrapolate_values_for_all(data)
    print(f"Sum of extrapolated values is {sum(values)}")
    previous_values = extrapolate_values_for_all(data, previous=True)
    print(f"Sum of extrapolated previous values is {sum(previous_values)}")


if __name__ == '__main__':
    main()


def test_extrapolate_values():
    assert extrapolate_values([0, 3, 6, 9, 12, 15,]) == 18
    assert extrapolate_values([1, 3, 6, 10, 15, 21]) == 28
    assert extrapolate_values([10, 13, 16, 21, 30, 45]) == 68


def test_extrapolate_previous_values():
    assert extrapolate_values([0, 3, 6, 9, 12, 15, ], previous=True) == -3
    assert extrapolate_values([1, 3, 6, 10, 15, 21], previous=True) == 0
    assert extrapolate_values([10, 13, 16, 21, 30, 45], previous=True) == 5
