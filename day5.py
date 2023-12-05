import re
from tqdm import tqdm


def solve():
    seeds = None
    with open("day5_input.txt") as f:
        file_str = f.read()
        seeds = [int(s) for s in re.match(r"seeds:((?: \d+)+)", file_str).groups()[0].split(" ")[1:]]
        matches = re.findall(r".*map:\n(?:\d+ \d+ \d+\n)+", file_str, re.MULTILINE)

    range_pattern = re.compile(r"(\d+) (\d+) (\d+)")
    transformers = []
    for match in matches:
        ranges = []
        lines = match.splitlines()[1:]
        for line in lines:
            m = range_pattern.match(line)
            dst, src, rng = m.group(1, 2, 3)
            ranges.append({"src": int(src), "dst": int(dst), "rng": int(rng)})
        transformers.append(ranges)

    result = []
    for seed in seeds:
        v = seed
        for transformer in transformers:
            for obj in transformer:
                if v >= obj["src"] and v < (obj["src"] + obj["rng"]):
                    v = (v - obj["src"]) + obj["dst"]
                    break
        result.append(v)

    return min(result)
    # return result

def solve_2():
    seeds = None
    with open("day5_input.txt") as f:
        file_str = f.read()
        seeds = [int(s) for s in re.match(r"seeds:((?: \d+)+)", file_str).groups()[0].split(" ")[1:]]
        matches = re.findall(r".*map:\n(?:\d+ \d+ \d+\n)+", file_str, re.MULTILINE)

    seed_ranges = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
    range_pattern = re.compile(r"(\d+) (\d+) (\d+)")
    transformers = []
    for match in matches:
        ranges = []
        lines = match.splitlines()[1:]
        for line in lines:
            m = range_pattern.match(line)
            dst, src, rng = m.group(1, 2, 3)
            ranges.append({"src": int(src), "dst": int(dst), "rng": int(rng)})
        transformers.append(ranges)

    lowest = 1000000000000
    transformers.reverse()
    for seed in tqdm(range(198620952)):
        v = seed
        for transformer in transformers:
            for obj in transformer:
                if v >= obj["dst"] and v < (obj["dst"] + obj["rng"]):
                    v = (v - obj["dst"]) + obj["src"]
                    break
        for low, length in seed_ranges:
            if v >= low and v < low + length and v < lowest:
                return seed

    return lowest
