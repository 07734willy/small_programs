from collections import Counter
from itertools import combinations

def num_of_kind(cards):
    return Counter(c[0] for c in cards)

def count_pairs(cards):
    return sum(i > 1 for i in num_of_kind(cards).values())

def largest_pair(cards):
    return max(num_of_kind(cards).values())

def is_straight(cards):
    values = [c[0] for c in cards]
    index = "A23456789TJQKA"["K" in values:].index
    indices = sorted(index(v) for v in values)
    return all(x == y for x, y in enumerate(indices, indices[0]))

def is_flush(cards):
    suit_pop = Counter(c[1] for c in cards)
    return any(s > 4 for s in suit_pop.values())

def straight_sort(cards):
    values = [c[0] for c in cards]
    index = "A23456789TJQKA"["K" in values:].index
    return sorted(cards, key=lambda x:index(x[0]), reverse=True)

def flush_sort(cards):
    suit_pop = Counter(c[1] for c in cards)
    return sorted(cards, key=lambda x: suit_pop[x[1]], reverse=True)

def pair_sort(cards):
    num = num_of_kind(cards)
    return sorted(cards, key=lambda x: num[x[0]], reverse=True)

def card_vals(cards):
    return [c[0] for c in cards]

def score_hand(cards):
    pairs = count_pairs(cards)
    largest = largest_pair(cards)
    straight = is_straight(cards)
    flush = is_flush(cards)
    
    cards = straight_sort(cards)
    hand_score = 0
    if flush and straight:
        hand_score, cards = 8, flush_sort(cards)
    elif largest == 4:
        hand_score, cards = 7, pair_sort(cards)
    elif pairs == 2 and largest == 3:
        hand_score, cards = 6, pair_sort(cards)
    elif flush:
        hand_score, cards = 5, flush_sort(cards)
    elif straight:
        hand_score = 4
    elif largest == 3:
        hand_score, cards = 3, pair_sort(cards)
    else:
        hand_score, cards = pairs, pair_sort(cards)
    return hand_score, card_vals(cards), cards

def best_hand(cards):
    cards = max(list(combinations(cards, 5)), key=score_hand)
    score, _, hand = score_hand(cards)
    return hand[::-1], score

def main():
    #hand = ['2c','Ah','3d', '5s','4h','5d', '3h']
    hand = ['2h','9h','3h','5s','4h','5h','3c']
    print(*best_hand(hand))

if __name__ == "__main__":
    main()
