import numpy as np
import pprint as pp


def are_rows_off_by_one(rows):
    r1, r2 = rows
    xor = int(r1, 2) ^ int(r2, 2)
    diffs = len([d for d in format(xor, 'b') if d == '1'])
    return diffs == 1


def find_reflections(pattern):
    for i in range(1, (len(pattern) // 2) + 1):
        slice_1 = pattern[:i]
        slice_2 = pattern[i : 2 * i][::-1]

        equal = True
        smudges = 0
        for rows in zip(slice_1, slice_2):
            r1, r2 = rows
            if r1 != r2:
                if are_rows_off_by_one(rows) and smudges == 0:
                    smudges += 1
                else:
                    equal = False

        if equal and smudges == 1:
            return i


def find_horizontal_reflections(pattern):
    if result := find_reflections(pattern):
        return result
    if result := find_reflections(pattern[::-1]):
        return len(pattern) - result


def find_vertical_reflections(pattern):
    flipped = list(map("".join, map(list, zip(*pattern))))
    if result := find_reflections(flipped):
        return result
    if result := find_reflections(flipped[::-1]):
        return len(flipped) - result


def symbols_to_binary(line):
    bin_str = "".join(["1" if ch == "#" else "0" for ch in line])
    return bin_str


def solve():
    patterns = None

    with open("day13_input.txt") as f:
        patterns = f.read().split("\n\n")

    total = 0
    bin_patterns = list(
        map(lambda p: [symbols_to_binary(i) for i in p.splitlines()], patterns)
    )
    for i, pattern in enumerate(bin_patterns):
        if horizontal_result := find_horizontal_reflections(pattern):
            total += 100 * horizontal_result
        if vertical_result := find_vertical_reflections(pattern):
            total += vertical_result

    return total


print(solve())
