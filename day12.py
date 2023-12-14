import re
from tqdm import tqdm

def score_string(springs, groups, spring_index, group_index, group_length, cache):
    key = (spring_index, group_index, group_length)
    
    v = cache.get(key)
    if v: 
        return v
    
    if spring_index == len(springs):
        if group_index == len(groups) and group_length == 0:
            return 1
        elif group_index == len(groups) - 1 and groups[group_index] == group_length:
            return 1
        else:
            return 0
    ans = 0
    
    for symbol in ['.', '#']:
        if springs[spring_index] == symbol or springs[spring_index] == '?':
            if symbol == '.' and group_length == 0:
                ans += score_string(springs, groups, spring_index + 1, group_index, 0, cache)
            elif symbol == '.' and group_length > 0 and group_index < len(groups) and groups[group_index] == group_length:
                ans += score_string(springs, groups, spring_index + 1, group_index + 1, 0, cache)
            elif symbol == '#':
                ans += score_string(springs, groups, spring_index + 1, group_index, group_length + 1, cache)

    cache[key] = ans
    return ans

def solve():
    lines = None
    with open("day12_input.txt") as f:
        lines = f.read().splitlines()

    parse_pattern = re.compile(r"(.+) (.+)")

    total = 0
    for line in tqdm(lines):
        m = parse_pattern.match(line)
        springs, description = m.group(1, 2)

        springs = "?".join([springs] * 5)
        description = ",".join([description] * 5)

        print(springs)
        print(description)

        groups = [int(ch) for ch in description.split(',')]


        possibilites = score_string(springs, groups, 0, 0, 0, {})

        total += possibilites
    return total

print(solve())
