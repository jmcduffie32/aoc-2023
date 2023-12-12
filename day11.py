import re
import pprint as pp
import numpy as np
from itertools import combinations

def pprint_matrix(matrix):
    print('\n'.join(map(''.join, matrix)))

def solve():
    lines = None
    with open("day11_input.txt") as f:
        lines = f.read().splitlines()

    result_lines = []

    # expansion_rate = 1
    expansion_rate = 1000000 - 1
    
    x_expansions = set()
    y_expansions = set()

    for i, line in enumerate(lines):
        chars = list(line)
        result_lines.append(chars)
        if line.find('#') == -1:
            y_expansions.add(i)
    
    transposed = np.transpose(result_lines)

    transposed_result = []

    for i, line in enumerate(transposed):
        transposed_result.append(line)
        if all(map(lambda x: x == '.', line)):
            x_expansions.add(i)

    result_lines = np.transpose(transposed_result) 

    locations = set()
    
    for i, line in enumerate(result_lines):
        for j, symbol in enumerate(line):
            if symbol == '#':
                locations.add((j, i))
    
    
    total = 0
    for locations in combinations(locations, 2):
        p1, p2 = locations
        x1, x2 = sorted([p1[0], p2[0]])
        y1, y2 = sorted([p1[1], p2[1]])
        distance = (x2 - x1) + (y2 - y1)
        x_expansions_in_range = [v for v in x_expansions if x1 < v and v < x2]
        y_expansions_in_range = [v for v in y_expansions if y1 < v and v < y2]
        distance += len(x_expansions_in_range) * expansion_rate
        distance += len(y_expansions_in_range) * expansion_rate
        total += distance
    
    return total

print(solve())
