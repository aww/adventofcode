

def read_input():
    with open('../private/2023/day04_scratch_cards_input.txt', 'r') as f:
        return f.readlines()


def get_winning_set(s: str) -> set:
    _, nums = s.split(':')
    win_str, have_str = nums.split('|')
    wins = set(map(int, win_str.strip().split()))
    haves = set(map(int, have_str.strip().split()))
    return haves.intersection(wins)


def card_count(matches: list[int]) -> int:
    """We get a list of numbers which is the number of matches per card.
    The number of matches N wins us new copies of the next N cards which can have matches
    which win additional copies of the subsequent cards in the same way.
    Return the total number of cards we end up at the end."""

    cards = list([1 for x in range(len(matches))])
    total = 0
    for i, m in enumerate(matches):
        for j in range(m):
            cards[min(i+j+1, len(cards))] += cards[i]
        total += cards[i]
    return total


def part1() -> int:
    score = 0
    for line in read_input():
        winning_set = get_winning_set(line)
        if len(winning_set) > 0:
            score += 2**(len(winning_set)-1)
    return score


def part2() -> int:
    match_count: list[int] = []
    for line in read_input():
        winning_set = get_winning_set(line)
        match_count.append(len(winning_set))
    cc = card_count(match_count)
    return cc


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
