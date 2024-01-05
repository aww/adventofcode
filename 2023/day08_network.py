import re
import itertools
import math
from collections import Counter


def read_documents(txt: str = None) -> tuple[str, dict[str, tuple[str, str]]]:
    if txt is None:
        with open('day08_network_input.txt', 'r') as f:
            txt = f.read()
    instr, network_txt = txt.split('\n\n')
    network: dict[str, tuple[str, str]] = {}
    for line in network_txt.strip().split('\n'):
        m = re.search(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)
        network[m.group(1)] = (m.group(2), m.group(3))
    return instr, network


def follow_instructions(instr: str, network: dict[str, tuple[str, str]]) -> int:
    steps = 0
    next = 'AAA'
    for i, c in enumerate(itertools.cycle(instr)):
        if c == 'L':
            next = network[next][0]
        else:
            next = network[next][1]
        steps += 1
        if next == 'ZZZ':
            break
    return steps


def prime_factor_helper(n: int, primes: dict[int, int]) -> tuple[int, dict[int, int]]:
    if n <= 1:
        return 1, primes
    if n % 2 == 0:
        primes[2] += 1
        return prime_factor_helper(n // 2, primes)
    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            primes[i] += 1
            return prime_factor_helper(n // i, primes)
    primes[n] += 1
    return 1, primes


def prime_factors(n: int) -> dict[int, int]:
    return prime_factor_helper(n, Counter())[1]


def lcm(ns: list[int]) -> int:
    factorizations = []
    for n in ns:
        factorizations.append(prime_factors(n))
    lcmfac = Counter()
    for fac in factorizations:
        for k, v in fac.items():
            if k not in lcmfac or lcmfac[k] < v:
                lcmfac[k] = v
    prod = 1
    for fac, pow in lcmfac.items():
        prod *= fac**pow
    return prod


def follow_instructions_many(instr: str, network: dict[str, tuple[str, str]]) -> int:
    steps = 0
    current = [x for x in network.keys() if x[-1] == 'A']
    cycle_lengths = [0] * len(current)
    for c in itertools.cycle(instr):
        if c == 'L':
            next = [network[x][0] for x in current]
        else:
            next = [network[x][1] for x in current]
        steps += 1
        for i, x in enumerate(next):
            if x[-1] == 'Z' and cycle_lengths[i] == 0:
                cycle_lengths[i] = steps
                # print(cycle_lengths)
                # print(lcm(cycle_lengths))
                if all([x != 0 for x in cycle_lengths]):
                    return lcm(cycle_lengths)
        if all([x[-1] == 'Z' for x in next]):
            break
        current = next
    return steps


def main():
    instr, network = read_documents()
    print(f"{len(instr)} instructions")
    print(f"{len(network)} nodes in the network")
    steps = follow_instructions(instr, network)
    print(f"{steps} steps from AAA to ZZZ")
    steps = follow_instructions_many(instr, network)
    print(f"{steps} steps using many paths from *A to *Z")


if __name__ == '__main__':
    main()


def test_read_documents():
    docs = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
    instr, network = read_documents(docs)
    assert instr == 'RL'
    assert network == {
        'AAA': ('BBB', 'CCC'),
        'BBB': ('DDD', 'EEE'),
        'CCC': ('ZZZ', 'GGG'),
        'DDD': ('DDD', 'DDD'),
        'EEE': ('EEE', 'EEE'),
        'GGG': ('GGG', 'GGG'),
        'ZZZ': ('ZZZ', 'ZZZ'),
    }


def test_follow_instructions():
    network = {
        'AAA': ('BBB', 'BBB'),
        'BBB': ('AAA', 'ZZZ'),
        'ZZZ': ('ZZZ', 'ZZZ'),
    }
    assert follow_instructions('LLR', network) == 6


def test_follow_instructions_many():
    instr, network = read_documents("""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""")
    assert follow_instructions_many(instr, network) == 6
