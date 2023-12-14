import re
import numpy as np


def row_load(line):
    max_load = len(line)
    current_load = max_load
    result = 0
    for i, symbol in enumerate(line):
        if symbol == "O":
            result += current_load
            current_load -= 1
        elif symbol == "#":
            current_load = max_load - (i + 1)

    return result


def tip_row(line):
    max_load = len(line)
    cursor = 0
    tipped_row = ["."] * max_load
    for i, symbol in enumerate(line):
        if symbol == "O":
            tipped_row[cursor] = "O"
            cursor += 1
        elif symbol == "#":
            tipped_row[i] = "#"
            cursor = i + 1

    return tipped_row

def solve():
    lines = None
    with open("day14_input.txt") as f:
        lines = list(map(lambda line: [ch for ch in line], f.read().splitlines()))

    lines = np.rot90(lines, k=1, axes=(0,1))
    result = 0
    for line in lines:
        result += row_load(line)

    print(lines)
    return result

def find_load(line):
    line_len = len(line)
    result = 0
    for i, ch in enumerate(line):
        if ch == 'O':
            result += line_len - i
    return result

def solve_2():
    lines = None
    with open("day14_input.txt") as f:
        lines = list(map(lambda line: [ch for ch in line], f.read().splitlines()))

    seen = {}
    for n in range(142):
        for j in range(4):
            axes = ((0, 1) if j == 0  else (1, 0))
            lines = np.rot90(lines, k=1, axes=axes)
            for i, line in enumerate(lines):
                lines[i] = tip_row(line)

        lines = np.rot90(lines, k=2, axes=(1,0))
        
        if v := seen.get(str(lines.tolist())):
            print("SEEN", n, v)
            break
        else:
            seen[str(lines.tolist())] = n
    
    lines = np.rot90(lines, k=1, axes=(0, 1))
    result = 0
    for line in lines:
        result += find_load(line)
    
    print("NORTH LOAD", result)
    return lines

solve_2()
# print("\n".join(list(map("".join,solve_2()))))
# print(solve())
