import re
from collections import defaultdict



def assign_type_score(hand):
    counts = defaultdict(lambda: 0) 
    for card in hand.cards:
        counts[card] += 1
    counts = tuple(sorted(counts.values()))
    scores = {
        (1, 1, 1, 1, 1): 1,
        (1, 1, 1, 2): 2,
        (1, 2, 2): 3,
        (1, 1, 3): 4,
        (1, 1, 3): 5,
        (2, 3): 6,
        (1, 4): 7,
        (5,): 8,
    }
    return scores[counts]

def assign_type_score_with_jacks(hand):
    counts = defaultdict(lambda: 0) 
    jack_count = 0
    for card in hand.cards:
        if card == 1:
            jack_count += 1
        else:
            counts[card] += 1
    counts = sorted(counts.values())
    scores = {
        (1, 1, 1, 1, 1): 1,
        (1, 1, 1, 2): 2,
        (1, 2, 2): 3,
        (1, 1, 3): 4,
        (1, 1, 3): 5,
        (2, 3): 6,
        (1, 4): 7,
        (5,): 8,
    }
    if jack_count == 5:
        return 8
    counts[-1] += jack_count
    counts = tuple(counts)
    return scores[counts]

# card_values = {
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     'T': 10,
#     'J': 11,
#     'Q': 12,
#     'K': 13,
#     'A': 14,
# }

card_values = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14,
}

class Hand:
    def __init__(self, hand_str):
        m = re.match(r"(\w+) (\d+)", hand_str)
        card_str, bid_str = m.group(1, 2)
        self.cards = [card_values[ch] for ch in card_str]
        self.bid = int(bid_str)
        # self.type_score = assign_type_score(self)
        self.type_score = assign_type_score_with_jacks(self)


def solve():
    lines = None
    with open("day7_input.txt") as f:
        lines = f.read().splitlines()
    
    hands = [Hand(line) for line in lines]

    hands.sort(key=lambda h: [h.type_score, h.cards])
    result = 0
    for i, hand in enumerate(hands):
        result += (i + 1) * hand.bid
    return result


print(solve())
