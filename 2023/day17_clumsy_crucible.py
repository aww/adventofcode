import numpy as np
from functools import total_ordering
from heapq import heappush, heappop


def read_input(s: str = None) -> np.ndarray:
    if s is None:
        with open('../private/2023/day17_crucible_input.txt', 'r') as f:
            lines = f.read().strip().splitlines()
    else:
        lines = s.strip().splitlines()
    return np.array([list(x) for x in lines], dtype=int)


DIRECTIONS = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


@total_ordering
class PathStepLoss:
    def __init__(self, step: tuple[int, int, int, int], loss: int, path=None) -> None:
        self.step, self.loss = step, loss
        if path is None:
            self.path = []
        else:
            self.path = path

    def __lt__(self, other: 'PathStepLoss') -> bool:
        return self.loss < other.loss

    def __str__(self) -> str:
        return f"{self.step}->{self.loss}"

    def printgrid(self, grid: np.ndarray) -> None:
        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                if self.step[0] == row and self.step[1] == col:
                    print({0: '>', 1: 'v', 2: '<', 3: '^'}[self.step[2]], end='')
                elif self.path is not None and (row, col) in [(x, y) for x, y, _, _ in self.path]:
                    print('#', end='')
                else:
                    print(grid[row][col], end='')
            if row == 0:
                print(f"  Loss = {self.loss}  Distance = {self.step[3]}")
            else:
                print()


def minimize(grid: np.ndarray, pathmin=0, pathmax=3, findpath=False) -> int:
    """For every cell we will fill it with a list of minimum heat losses L given
    the path came N steps from the direction D={N,W,S,E}:
    {D1: [(N11, L11), (N12, L12)], D2: [(N21, L21), (N22, L22)] ... }
    A cell is fully visited when there are values from every possible direction"""
    nrow, ncol = grid.shape
    minimums = {}
    # This is the bit that hung me up for a while.
    # I basically wanted a heap queue for the frontier but didn't know the name.
    # After some other messier implementations I finally did the right searches and found the heapq package.
    # The only wrinkle is it doesn't provide a key= option so PathStepLoss was created to order steps by loss.
    frontier = []

    def explore(x, y, d, n, prevloss, prev=None) -> None:
        if x < 0 or y < 0 or x >= nrow or y >= ncol:
            return
        pathstep = (x, y, d, n)
        if pathstep not in minimums:
            loss = prevloss + grid[x][y]
            heappush(frontier, PathStepLoss(pathstep, loss, path=None if prev is None else prev.path + [pathstep]))
            minimums[pathstep] = loss
            # print(f"Pushed: {pathstep=} {loss=} " + " ".join([str(psl) for psl in frontier]))

    # The negative losses here are kind of hacky, but I tried reorganizing my code and couldn't get that to work.
    # Not counting the losses from the first position as specified in the problem seems equally hacky,
    # so I'm going with this.
    # Also: I was using np.uint8 for the loss array but switched to signed int
    #  * because of "overflow encountered in scalar negative" warning, and
    #  * because losses get bigger than 8-bits in my input (should have forseen this).
    #    (Thanks for the warnings, Python!)
    explore(0, 0, 0, 1, -grid[0][0])
    explore(0, 0, 1, 1, -grid[0][0])

    while len(frontier) > 0:
        # print("Frontier: " + " ".join([str(psl) for psl in frontier]))
        minitem = heappop(frontier)
        # print(f"Popped: {minitem}")
        # minitem.printgrid(grid)
        x, y, d, n = minitem.step
        loss = minitem.loss
        if x == nrow - 1 and y == ncol - 1 and n > pathmin:
            return loss
        xprime, yprime = x + DIRECTIONS[d][0], y + DIRECTIONS[d][1]
        if n < pathmax:
            explore(xprime, yprime, d, n+1, loss, prev=minitem if findpath else None)
        if n >= pathmin:
            explore(xprime, yprime, (d+1) % 4, 1, loss, prev=minitem if findpath else None)
            explore(xprime, yprime, (d-1) % 4, 1, loss, prev=minitem if findpath else None)

    raise ValueError("Ran out of steps without finding target.")


def part1() -> int:
    grid = read_input()
    mloss = minimize(grid, pathmax=3)
    return mloss


def part2() -> int:
    grid = read_input()
    mloss = minimize(grid, pathmin=4, pathmax=10)
    return mloss


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
