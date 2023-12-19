import re
from collections import OrderedDict

def special_hash(str: str):
    current_value = 0

    for ch in str:
        current_value += ord(ch)
        current_value *= 17
        current_value = current_value % 256
    
    return current_value

def read_input():
    with open("day15_input.txt") as f:
        return f.read().replace("\n", "")

def solve():
    input = read_input()

    return sum([special_hash(instruction) for instruction in input.split(",")])

def add_item(boxes: list[OrderedDict], index: int, prefix: str, value: str):
    boxes[index][prefix] = int(value)

def remove_item(boxes: list[OrderedDict], index: int, prefix: str):
    if boxes[index].get(prefix):
        del boxes[index][prefix]
        
def solve_2():
    input = read_input()
     
    boxes = [OrderedDict() for i in range(256)]

    p = re.compile(r"(.*)(-|=)(.*)")
    for instruction in input.split(","):
        m = p.match(instruction)
        label, op, value = m.group(1,2,3)
        index = special_hash(label)
        
        if op == '=':
            add_item(boxes, index, label, value)
        else:
            remove_item(boxes, index, label)

    total = 0
    for i, box in enumerate(boxes): 
        box_score = i + 1
        for j, v in enumerate(box.values()):
            total += box_score * (j + 1) * v

    return total

print(solve_2())

