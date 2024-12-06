


def read_input(s: str = None) -> list[list]:
    reports = []
    if s is None:
        with open('../private/2024/day02_rednosed_reports_input.txt', 'r') as f:
            s = f.read()
    for line in s.splitlines():
        line = line.strip()
        if len(line) > 0:
            report = list(map(int, line.split()))
            reports.append(report)
    return reports


def is_gradual(a: int, b: int) -> bool:
    return abs(a - b) > 0 and abs(a - b) < 4


def is_report_safe(lst: list) -> bool:
    direction = None
    for prv, nxt in zip(lst, lst[1:]):
        if not is_gradual(prv, nxt):
            return False
        if prv < nxt:
            if direction is None:
                direction = 1
            else:
                if direction != 1:
                    return False
        else:
            if direction is None:
                direction = -1
            else:
                if direction != -1:
                    return False
    return True


def eliminate_element(lst: list, i: int):
    return lst[:i] + lst[i+1:]


def is_report_safe_dampened(lst: list) -> bool:
    if is_report_safe(lst):
        return True
    return any([is_report_safe(eliminate_element(lst, i)) for i in range(len(lst))])


def part1() -> int:
    reports = read_input()
    safe_count = 0
    for r in reports:
        if is_report_safe(r):
            safe_count += 1
    return safe_count


def part2() -> int:
    reports = read_input()
    safe_count = 0
    for r in reports:
        if is_report_safe_dampened(r):
            safe_count += 1
    return safe_count


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
