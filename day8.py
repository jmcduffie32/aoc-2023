from copy import deepcopy
from math import lcm
import re


class Node:
    def __init__(self, id, left_str, right_str):
        self.id = id
        self.left_str = left_str
        self.right_str = right_str
        self.left = None
        self.right = None




def solve():
    lines = None
    with open("day8_input.txt") as f:
        lines = f.read().splitlines()
    
    directions = [ch for ch in lines[0]]
    node_strs = lines[2:]

    node_map = {} 

    p = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
    for node_str in node_strs:
        m = p.match(node_str)
        id, left_str, right_str = m.group(1,2,3)
        node_map[id] = Node(id, left_str, right_str)

    for id in node_map.keys():
        node = node_map[id]
        node.left = node_map[node.left_str]
        node.right = node_map[node.right_str]

    starting_node = node_map['AAA']
    current_node = starting_node

    step_count = 0
    while current_node.id != 'ZZZ':
        if directions[step_count % len(directions)] == 'L':
            current_node = current_node.left
        else:
            current_node = current_node.right
        step_count += 1
    return step_count

def are_all_nodes_complete(nodes):
    return all([node.id[-1] == 'Z' for node in nodes])

def solve_2():
    lines = None
    with open("day8_input.txt") as f:
        lines = f.read().splitlines()
    
    directions = [ch for ch in lines[0]]
    node_strs = lines[2:]

    node_map = {} 

    p = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
    for node_str in node_strs:
        m = p.match(node_str)
        id, left_str, right_str = m.group(1,2,3)
        node_map[id] = Node(id, left_str, right_str)

    for id in node_map.keys():
        node = node_map[id]
        node.left = node_map[node.left_str]
        node.right = node_map[node.right_str]

    starting_nodes = [node_map[id] for id in node_map.keys() if id[-1] == 'A']
    current_nodes = starting_nodes

    step_counts = []
    for node in starting_nodes:
        step_count = 0
        current_node = deepcopy(node)
        while current_node.id[-1] != 'Z':
            if directions[step_count % len(directions)] == 'L':
                current_node = current_node.left
            else:
                current_node = current_node.right
            step_count += 1
        step_counts.append(step_count)

    return lcm(*step_counts)


print(solve_2())    

