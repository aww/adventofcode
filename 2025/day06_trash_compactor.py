def read_input(s: str | None = None) -> tuple[list[list[int]], list[str]]:
    rows: list[list[int]] = []
    if s is None:
        with open("../private/2025/day06_trash_compactor_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            items = line.split()
            if items[0] == "*" or items[0] == "+":
                return rows, items
            else:
                rows.append(list(map(int, items)))
    raise ValueError("Never found an operator row in the input (at the end).")


def read_input_part2(s: str | None = None) -> tuple[list[str], list[str]]:
    columns: list[str] = []
    if s is None:
        with open("../private/2025/day06_trash_compactor_input.txt", "r") as f:
            s = f.read()
    for line in s.splitlines():
        if line.strip() == "":
            continue
        if line[0] == "+" or line[0] == "*":
            return columns, line.split()
        else:
            for i, c in enumerate(line):
                if len(columns) == i:
                    columns.append("")
                columns[i] += c
    raise ValueError("Never found an operator row in the input (at the end).")


def domath(nums: list[list[int]], ops: list[str]) -> int:
    problems = nums[0]
    for row in nums[1:]:
        for i, (op, val) in enumerate(zip(ops, row)):
            if op == "+":
                problems[i] += val
            elif op == "*":
                problems[i] *= val
            else:
                raise ValueError(f"Unrecognized operator '{op}'")
    grandtotal = sum(problems)
    return grandtotal


def docolmath(cols: list[str], ops: list[str]) -> int:
    iop = 0
    grandtotal = 0
    problemtotal = 0
    if ops[0] == "*":
        problemtotal = 1
    for txt in cols:
        if txt.strip() == "":
            grandtotal += problemtotal
            iop += 1
            problemtotal = 0
            if ops[iop] == "*":
                problemtotal = 1
        else:
            if ops[iop] == "+":
                problemtotal += int(txt)
            elif ops[iop] == "*":
                problemtotal *= int(txt)
            else:
                raise ValueError(f"Unrecognized operator '{ops[iop]}'")
    grandtotal += problemtotal
    if iop >= len(ops):
        raise ValueError("Found more column groups than operators")
    return grandtotal


def part1() -> int:
    nums, ops = read_input()
    return domath(nums, ops)


def part2() -> int:
    cols, ops = read_input_part2()
    return docolmath(cols, ops)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
