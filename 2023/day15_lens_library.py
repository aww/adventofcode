

def read_input(s: str = None) -> list[str]:
    if s is None:
        with open('../private/2023/day15_hash_input.txt', 'r') as f:
            return f.read().strip().split(',')
    else:
        return s.strip().split(',')


def hashstr(s: str) -> int:
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def hashsumseq(seq: list[str]) -> int:
    hashsum = 0
    for s in seq:
        hashsum += hashstr(s)
    return hashsum


class Box:
    def __init__(self):
        self.queue = {}  # dict is ordered by insertion in modern python versions

    def insert(self, label: str, focallength: int) -> None:
        self.queue[label] = focallength

    def remove(self, label: str) -> None:
        if label in self.queue:
            del self.queue[label]

    def slotflprodsum(self) -> int:
        total = 0
        for slot, focallength in enumerate(self.queue.values()):
            total += (slot + 1) * focallength
        return total

    def __len__(self) -> int:
        return len(self.queue)

    def __str__(self) -> str:
        result = []
        for label, fl in self.queue.items():
            result.append(f"[{label} {fl}]")
        return ' '.join(result)


class Hashmapper:
    def __init__(self, seq: list[str] = None):
        self.boxes = [Box() for _ in range(256)]
        if seq is not None:
            for op in seq:
                self.op(op)

    def op(self, opstr: str):
        if (eqidx := opstr.find('=')) != -1:
            label, focallength = opstr[:eqidx], opstr[eqidx+1:]
            # print(f"{eqidx=}, {label=}, {focallength=}")
            focallength = int(focallength)
            h = hashstr(label)
            self.boxes[h].insert(label, focallength)
        elif (dashidx := opstr.find('-')) != -1:
            label = opstr[:dashidx]
            h = hashstr(label)
            self.boxes[h].remove(label)
        else:
            raise ValueError(f"Invalid operation '{opstr}'")

    def focusingpower(self) -> int:
        total = 0
        for boxpos in range(len(self.boxes)):
            total += (boxpos + 1) * self.boxes[boxpos].slotflprodsum()
        return total

    def __str__(self) -> str:
        result = []
        for boxpos in range(len(self.boxes)):
            box = self.boxes[boxpos]
            if len(box) > 0:
                result.append(f"Box {boxpos}: {box}")
        return "\n".join(result)


def part1() -> int:
    seq = read_input()
    hashsum = hashsumseq(seq)
    return hashsum


def part2() -> int:
    seq = read_input()
    hm = Hashmapper(seq)
    return hm.focusingpower()


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
