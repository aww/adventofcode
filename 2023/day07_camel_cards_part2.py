from collections import Counter


def read_cards(txt: str = None) -> list[tuple[str, int]]:
    if txt is None:
        with open('day07_camel_cards_input.txt', 'r') as f:
            txt = f.read()
    result = []
    for line in txt.strip().split('\n'):
        a, b = line.split()
        result.append((a, int(b)))
    return result


def hand_type_key(hand: str):
    cnt = Counter(hand)
    # The len(cnt) > 1 condition ensures there is another card.
    # If it is all jokers then we just leave the counts alone (it is already 5 of a kind)
    if 'J' in cnt and len(cnt) > 1:
        njokers = cnt.pop('J')
        mostcommon = cnt.most_common(1)
        cnt[mostcommon[0][0]] += njokers
    sig = tuple([x[1] for x in cnt.most_common()])
    return sig


CARD_ORDER_TRANS = str.maketrans('TJQKA', 'a1cde')


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


def main():
    hands = read_cards()
    sorted_hands = sort_hands(hands)
    score = score_hands(sorted_hands)
    print(f"Score of {score}")


if __name__ == '__main__':
    main()


def test_read_cards():
    sample = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    assert read_cards(sample) == [
        ('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)
    ]


def test_hand_type_key():
    assert hand_type_key('32T3K') == (2, 1, 1, 1)
    assert hand_type_key('T55J5') == (4, 1)
    assert hand_type_key('KK677') == (2, 2, 1)
    assert hand_type_key('KTJJT') == (4, 1)
    assert hand_type_key('QQQJA') == (4, 1)
    assert hand_type_key('33333') == (5,)
    assert hand_type_key('33A33') == (4, 1)


def test_hand_strength_key():
    assert hand_strength_key('32T3K') == '32a3d'
    assert hand_strength_key('T55J5') == 'a5515'
    assert hand_strength_key('KK677') == 'dd677'
    assert hand_strength_key('KTJJT') == 'da11a'
    assert hand_strength_key('QQQJA') == 'ccc1e'


def test_sort_hands():
    sample = [
        ('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)
    ]
    assert sort_hands(sample) == [
        ('32T3K', 765), ('KK677', 28), ('T55J5', 684), ('QQQJA', 483), ('KTJJT', 220),
    ]


def test_score_hands():
    sample = [('A', 765), ('B', 28), ('C', 684), ('D', 483), ('E', 220)]
    assert score_hands(sample) == 5905
