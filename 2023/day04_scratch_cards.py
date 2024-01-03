fn = 'day04a_scratch_cards_input.txt'


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


if __name__ == '__main__':
    with open(fn, 'r') as f:
        match_count: list[int] = []
        score = 0
        for line in f:
            winning_set = get_winning_set(line)
            match_count.append(len(winning_set))
            if len(winning_set) > 0:
                score += 2**(len(winning_set)-1)
        print(f'"Score" = {score}')
        cc = card_count(match_count)
        print(f'Total card count = {cc}')

def test_length_winning_set():
    assert get_winning_set("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == {48, 83, 17, 86}
    assert get_winning_set("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19") == {32, 61}
    assert get_winning_set("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1") == {1, 21}
    assert get_winning_set("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83") == {84}
    assert get_winning_set("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36") == set()
    assert get_winning_set("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11") == set()

def test_card_count():
    assert card_count([4, 2, 2, 1, 0, 0]) == 30
