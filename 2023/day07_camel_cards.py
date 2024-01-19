from collections import Counter


def read_cards(txt: str = None) -> list[tuple[str, int]]:
    if txt is None:
        with open('../private/2023/day07_camel_cards_input.txt', 'r') as f:
            txt = f.read()
    result = []
    for line in txt.strip().split('\n'):
        a, b = line.split()
        result.append((a, int(b)))
    return result


def hand_type_key(hand: str):
    cnt = Counter(hand)
    sig = tuple([x[1] for x in cnt.most_common()])
    return sig


CARD_ORDER_TRANS = str.maketrans('TJQKA', 'abcde')


def hand_strength_key(hand: str) -> str:
    return hand.translate(CARD_ORDER_TRANS)


def sort_hands(hands: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(sorted(hands,
                         key=lambda x: hand_strength_key(x[0])),
                  key=lambda x: hand_type_key(x[0]))


def score_hands(hands: list[tuple[str, int]]) -> int:
    """Hands are assumed to be sorted in ascending order.
    The score is the sum of bids (second entry) multiplied by rank starting with 1."""
    return sum([(i+1)*bid for i, (_, bid) in enumerate(hands)])


def hand_type_joker_key(hand: str):
    cnt = Counter(hand)
    # The len(cnt) > 1 condition ensures there is another card.
    # If it is all jokers then we just leave the counts alone (it is already 5 of a kind)
    if 'J' in cnt and len(cnt) > 1:
        njokers = cnt.pop('J')
        mostcommon = cnt.most_common(1)
        cnt[mostcommon[0][0]] += njokers
    sig = tuple([x[1] for x in cnt.most_common()])
    return sig


CARD_ORDER_JOKER_TRANS = str.maketrans('TJQKA', 'a1cde')


def hand_strength_joker_key(hand: str) -> str:
    return hand.translate(CARD_ORDER_JOKER_TRANS)


def sort_hands_joker(hands: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(sorted(hands,
                         key=lambda x: hand_strength_joker_key(x[0])),
                  key=lambda x: hand_type_joker_key(x[0]))


def part1() -> int:
    hands = read_cards()
    sorted_hands = sort_hands(hands)
    score = score_hands(sorted_hands)
    return score


def part2() -> int:
    hands = read_cards()
    sorted_hands = sort_hands_joker(hands)
    score = score_hands(sorted_hands)
    return score


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
