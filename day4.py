import re


def solve():
    lines = None
    with open("day4_input.txt") as f:
        lines = f.read().splitlines()

    cards = []
    p = re.compile(r"Card  ? ?\d+:((?: {1,2}\d+)+) \|((?: {1,2}\d+)+)")
    points = []
    for line in lines:
        m = p.match(line)
        if not m:
            print(line)
        winning_numbers, numbers = m.group(1, 2)
        winning_numbers = [int(s) for s in winning_numbers.split(" ") if s != ""]
        numbers = [int(s) for s in numbers.split(" ") if s != ""]


        winning_count = 0
        for number in numbers:
            if number in winning_numbers:
                winning_count += 1

        points.append(0 if winning_count == 0 else 2**(winning_count - 1))
    
    total = 0
    for p in points:
        total += p
    return total

def solve_2():
    lines = None
    with open("day4_input.txt") as f:
        lines = f.read().splitlines()

    cards = []
    p = re.compile(r"Card  ? ?\d+:((?: {1,2}\d+)+) \|((?: {1,2}\d+)+)")
    cards = {}
    for i, line in enumerate(lines):
        m = p.match(line)
        if not m:
            print(line)
        winning_numbers, numbers = m.group(1, 2)
        winning_numbers = [int(s) for s in winning_numbers.split(" ") if s != ""]
        numbers = [int(s) for s in numbers.split(" ") if s != ""]


        winning_count = 0
        for number in numbers:
            if number in winning_numbers:
                winning_count += 1

        if cards.get(i):
            cards[i] += 1
        else:
            cards[i] = 1

        for j in range(winning_count):
            index = i + j + 1
            if cards.get(index):
                cards[index] = cards[index] + cards[i]
            else:
                cards[index] = cards[i]

    total = 0
    print(cards)
    for v in cards.values():
        total += v

    return total

print(solve_2())
