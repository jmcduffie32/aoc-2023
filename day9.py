import re
from functools import reduce


def solve():
    lines = None
    with open("day9_input.txt") as f:
        lines = f.read().splitlines()

    p = re.compile(r"(-?\d+)")
    next_vals = []
    for line in lines:
        diffs = []
        digit_strs = re.findall(p, line)
        numbers = [int(s) for s in digit_strs]
        diffs.append(numbers)
        while not all(map(lambda x: x == 0, diffs[-1])):
            current_diff = diffs[-1]
            next_diffs = [current_diff[i + 1] - current_diff[i] for i in range(len(current_diff) - 1) ]
            diffs.append(next_diffs)
        if len(diffs[-1]) == 0:
            diffs[-1] = [0]

        next_vals.append(sum([diff[-1] for diff in diffs]))

    return sum(next_vals)

def solve_2():
    lines = None
    with open("day9_input.txt") as f:
        lines = f.read().splitlines()

    p = re.compile(r"(-?\d+)")
    next_vals = []
    for line in lines:
        diffs = []
        digit_strs = re.findall(p, line)
        numbers = [int(s) for s in digit_strs][::-1]
        diffs.append(numbers)
        while not all(map(lambda x: x == 0, diffs[-1])):
            current_diff = diffs[-1]
            next_diffs = [current_diff[i + 1] - current_diff[i] for i in range(len(current_diff) - 1) ]
            diffs.append(next_diffs)
        if len(diffs[-1]) == 0:
            diffs[-1] = [0]

        next_vals.append(sum([diff[-1] for diff in diffs]))

    return sum(next_vals)

print(solve_2())
