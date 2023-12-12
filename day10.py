import re
import pprint


class Node:
    def __init__(self, location, symbol):
        self.location = location
        self.symbol = symbol
        self.connection_1, self.connection_2 = self.build_connections(location, symbol)

    def build_connections(self, location, symbol):
        symbol_to_offsets = {
            "|": ((0, 1), (0, -1)),
            "-": ((1, 0), (-1, 0)),
            "7": ((0, 1), (-1, 0)),
            # "S": ((0, 1), (-1, 0)),
            "F": ((0, 1), (1, 0)),
            # "S": ((0, 1), (1, 0)),
            "L": ((1, 0), (0, -1)),
            "S": ((1, 0), (0, -1)),
            "J": ((-1, 0), (0, -1)),
        }

        (x1, y1), (x2, y2) = symbol_to_offsets[symbol]
        x, y = location
        return [(x + x1, y + y1), (x + x2, y + y2)]


def solve():
    lines = None
    with open("day10_input.txt") as f:
        lines = f.read().splitlines()

    starting_location = (0, 0)
    locations = {}
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            if symbol == ".":
                continue
            location = (x, y)
            locations[location] = Node(location, symbol)
            if symbol == "S":
                starting_location = location

    path_length = 0
    current_node = locations[starting_location]
    previous_node = current_node

    path_locations = {starting_location}

    while current_node.symbol != "S" or path_length == 0:
        next_location = (
            current_node.connection_1
            if current_node.connection_1 != previous_node.location
            else current_node.connection_2
        )
        path_locations.add(next_location)

        previous_node = current_node
        current_node = locations[next_location]
        path_length += 1

    return path_length / 2


# print(solve())


def solve_2():
    lines = None
    with open("day10_input.txt") as f:
        lines = f.read().splitlines()


    starting_location = (0, 0)
    locations = {}
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            if symbol == ".":
                continue
            location = (x, y)
            locations[location] = Node(location, symbol)
            if symbol == "S":
                starting_location = location

    path_length = 0
    current_node = locations[starting_location]
    previous_node = current_node

    path_locations = {starting_location}

    while current_node.symbol != "S" or path_length == 0:
        next_location = (
            current_node.connection_1
            if current_node.connection_1 != previous_node.location
            else current_node.connection_2
        )
        path_locations.add(next_location)

        previous_node = current_node
        current_node = locations[next_location]
        path_length += 1


    inside_count = 0
    result = []
    for y, line in enumerate(lines):
        vertical_count = 0
        turn_count = 0
        result_line = []
        for x, symbol in enumerate(line):
            # if symbol == "." and vertical_count % 2 == 1:
            if (x, y) not in path_locations:
                if vertical_count % 2 == 1:
                    inside_count += 1
                    result_line.append("I")
                else:
                    result_line.append('O')
            elif symbol in ["|", "J", "L", "S"]:
                vertical_count += 1
                result_line.append(symbol)
            elif symbol in ["7", "F"]:
                result_line.append(symbol)
            elif symbol == "-":
                result_line.append(symbol)
            else:
                result_line.append("O")
        print("".join(result_line))

    return inside_count


print(solve_2())
