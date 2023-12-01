import re


def solve():
    str_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }
    lines = None
    with open("day1_input.txt") as f:
        lines = f.read().splitlines()

    # p = re.compile(r"\d")
    p = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    sum = 0

    for line in lines:
        digits = p.findall(line)
        digit_1 = str_to_int.get(digits[0])
        digit_2 = str_to_int.get(digits[-1])
        code = int(f"{digit_1}{digit_2}")
        sum += code

    return sum


if __name__ == "__main__":
    print(solve())
