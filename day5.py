import re


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

print(solve())
