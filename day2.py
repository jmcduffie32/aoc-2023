import re

def solve():
    lines = None
    with open("day2_input.txt") as f:
        lines = f.read().splitlines()

    totals = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    p = re.compile(r"Game (\d+): (.*)")
    p_color = re.compile(r"(\d+) (red|green|blue)")
    possible_count = 0
    total_power = 0

    for i, line in enumerate(lines):
        m = p.match(line)
        game_id, game_desc = m.group(1, 2)
        game_id = int(game_id)
        draws = game_desc.split(";")
        possible = True

        max_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for draw in draws:

            matches = p_color.finditer(draw)
            for match in matches:
                n, color = match.group(1, 2)
                if max_colors.get(color) < int(n):
                    max_colors[color] = int(n)
                if totals.get(color) < int(n):
                    possible = False

        if possible == True:
            possible_count += game_id

        total_power += max_colors.get("red") * max_colors.get("green") * max_colors.get("blue")

    # return possible_count
    return total_power


if __name__ == '__main__':
    print(solve())


