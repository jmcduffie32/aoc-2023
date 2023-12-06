import re
from tqdm import tqdm


def solve():
    times = [54, 70, 82, 75]
    distances = [239, 1142, 1295, 1253]

    wins_list = []
    for i, time in enumerate(times):
        wins = 0
        distance = distances[i]
        for t in range(time):
            if (time - t) * t > distance:
                wins += 1
        wins_list.append(wins)

    result = 1
    for wins in wins_list:
        result *= wins
    return result

# print(solve())

def solve_2():
    wins = 0
    time = 54708275
    distance = 239114212951253
    for t in tqdm(range(time)):
        if (time - t) * t > distance:
                wins += 1
    return wins

print(solve_2())
