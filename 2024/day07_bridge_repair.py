import itertools


def read_input(s: str = None) -> list[str]:
    rows = []
    if s is None:
        with open('../private/2024/day07_bridge_repair_input.txt', 'r') as f:
            s = f.read()
    equations = []
    for line in s.strip().splitlines():
        line = line.strip()
        calibstr, numstr = line.split(': ')
        calib = int(calibstr)
        numlist = list(map(int, numstr.split()))
        equations.append((calib, numlist))
    return equations


def apply_operators(nums, ops):
    for opseq in itertools.product(ops, repeat=len(nums)-1):
        value = nums[0]
        for i, op in enumerate(opseq):
            value = op(value, nums[i+1])
        yield value


def total_calibration_result(equations) -> int:
    ops = [lambda x,y: x+y, lambda x,y: x*y]
    total = 0
    for calib, nums in equations:
        for value in apply_operators(nums, ops):
            if calib == value:
                total += calib
                break
    return total


def total_calibration_result2(equations) -> int:
    ops = [lambda x,y: x+y, lambda x,y: x*y, lambda x,y: int(str(x)+str(y))]
    total = 0
    for calib, nums in equations:
        for value in apply_operators(nums, ops):
            if calib == value:
                total += calib
                break
    return total


def part1() -> int:
    equations = read_input()
    return total_calibration_result(equations)


def part2() -> int:
    equations = read_input()
    return total_calibration_result2(equations)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
