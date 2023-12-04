import re


def is_symbol(chars, i, j):
    result = False
    try:
        val = chars[i][j]
        result = not (val.isdigit() or val.isalpha() or val == ".")
    except IndexError:
        result = False

    return result


def solve():
    lines = None
    with open("day3_input.txt") as f:
        lines = f.read().splitlines()

    chars = [[*line] for line in lines]

    current_digits = ""
    is_part = False
    sum = 0

    gears = {}
    g = []

    for i in range(len(chars)):
        if len(current_digits) != 0 and is_part:
            sum += int(current_digits)
        is_part = False
        g = []
        current_digits = ""
        for j in range(len(chars[0])):
            curr = chars[i][j]
            if curr.isdigit():
                current_digits += chars[i][j]
                indexes = [
                    [i + 1, j],
                    [i + 1, j + 1],
                    [i + 1, j - 1],
                    [i - 1, j],
                    [i - 1, j + 1],
                    [i - 1, j - 1],
                    [i, j - 1],
                    [i, j + 1],
                ]
                for k, l in indexes:
                    if is_symbol(chars, k, l):
                        is_part = True
                    try:
                        if chars[k][l] == '*' and (k, l) not in g:
                            g.append((k, l))
                    except:
                        pass

            else:
                if len(current_digits) != 0 and is_part:
                    sum += int(current_digits)
                if len(current_digits) != 0 and len(g) != 0:
                    for el in g:
                        if gears.get(el):
                            gears[el].append(int(current_digits))
                        else:
                            gears[el] = [int(current_digits)]
                is_part = False
                current_digits = ""
                g = []

    gear_total = 0
    for gear in gears.values():
        if len(gear) == 2:
            gear_total += gear[0] * gear[1]
    return gear_total
    # return sum


print(solve())
