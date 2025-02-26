from collections import defaultdict


def split_order(txt: str) -> tuple[int, int]:
    a, b = txt.strip().split("|")
    return int(a), int(b)


def split_update(txt: str) -> list[int]:
    seq = txt.strip().split(",")
    return list([int(x) for x in seq])


def read_input(s: str | None = None) -> tuple[list[tuple[int, int]], list[list[int]]]:
    if s is None:
        with open("../private/2024/day05_print_queue_input.txt", "r") as f:
            s = f.read()
    txt_orders, txt_updates = s.strip().split("\n\n")
    orders = list(map(split_order, txt_orders.splitlines()))
    updates = list(map(split_update, txt_updates.splitlines()))
    return orders, updates


def middle_number(seq):
    return seq[len(seq) // 2]


class OrderRules:
    def __init__(self, orders):
        self.after = defaultdict(set)
        for a, b in orders:
            self.after[a].add(b)

    def check(self, seq):
        prev = set()
        for s in seq:
            if s in self.after:
                afters = self.after[s]
                # print(f"Checking for {s} which must have {afters} only after")
                if len(afters & prev) > 0:
                    # print(f"FAILURE: {seq}")
                    return False
            prev.add(s)
        # print(f"Success: {seq}")
        return True

    def corrected(self, seq):
        prev = set()  # Tracks what values are previous to the current one
        is_corrected = False
        i = 0
        while i < len(seq):
            s = seq[i]
            if s in self.after:
                afters = self.after[s]
                must_move = afters & prev
                if len(must_move) > 0:
                    # There are previous values that must move forward of current value
                    is_corrected = True
                    for j in reversed(range(i)):
                        # Work backward so indexes don't change
                        # If this one moves pop it, decrement i, and insert it forward
                        x = seq[j]
                        if x in must_move:
                            seq.insert(i, seq.pop(j))
                            i -= 1
                            prev.discard(
                                x
                            )  # Update prev, presumes we will move all instances
            prev.add(s)
            i += 1
        if is_corrected:
            return seq
        else:
            return False


def sum_middle_correct(orders, updates):
    rules = OrderRules(orders)
    sum = 0
    for u in updates:
        if rules.check(u):
            sum += middle_number(u)
    return sum


def sum_middle_corrected(orders, updates):
    rules = OrderRules(orders)
    sum = 0
    for u in updates:
        corrected = rules.corrected(u)
        if corrected:
            sum += middle_number(u)
    return sum


def part1() -> int:
    orders, updates = read_input()
    return sum_middle_correct(orders, updates)


def part2() -> int:
    orders, updates = read_input()
    return sum_middle_corrected(orders, updates)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
