import itertools

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

class Cell:
    def __init__(self, row, col, symbol):
        self.row = row
        self.col = col
        self.symbol = symbol


class Beam:
    def __init__(self, position, direction):
        self.active = True
        self.position = position
        self.direction = direction

def active_beams(beams):
    active = [beam for beam in beams if beam.active]
    if len(active) == 0:
        return None
    else:
        return active

def move(beam: Beam, direction):
    row, col = beam.position
    beam.position = (row + direction[0], col + direction[1])

def get_current_cell(cells, row, col):
    if row < 0 or col < 0:
        return None
    try:
        current_cell = cells[row][col]
        return current_cell
    except:
        return None


def count_visited(cells, starting_beam):
    beams = [starting_beam]
    visited = set()
    
    while beams_to_move := active_beams(beams):
        for beam in beams_to_move:
            row, col = beam.position
            current_direction = beam.direction
            current_cell = get_current_cell(cells, row, col)

            if not current_cell or (current_cell, current_direction) in visited:
                beam.active = False
                break
            else:
                visited.add((current_cell, beam.direction))

            if current_cell.symbol in [".", "\\", "/"]:
                if current_cell.symbol == "\\":
                    if beam.direction == RIGHT: beam.direction = DOWN
                    elif beam.direction == LEFT: beam.direction = UP
                    elif beam.direction == UP: beam.direction = LEFT
                    elif beam.direction == DOWN: beam.direction = RIGHT
                elif current_cell.symbol == "/":
                    if beam.direction == RIGHT: beam.direction = UP
                    elif beam.direction == LEFT: beam.direction = DOWN
                    elif beam.direction == UP: beam.direction = RIGHT
                    elif beam.direction == DOWN: beam.direction = LEFT
                move(beam, beam.direction)
            elif current_cell.symbol == "|" and current_direction in [UP, DOWN]:
                move(beam, beam.direction)
            elif current_cell.symbol == "-" and current_direction in [LEFT, RIGHT]:
                move(beam, beam.direction)
            elif current_cell.symbol == "-":
                beam.direction = RIGHT
                new_beam = Beam(beam.position, LEFT)
                move(beam, beam.direction)
                move(new_beam, new_beam.direction)
                beams.append(new_beam)
            elif current_cell.symbol == "|":
                beam.direction = UP
                new_beam = Beam(beam.position, DOWN)
                move(beam, beam.direction)
                move(new_beam, new_beam.direction)
                beams.append(new_beam)
    return len(set(list(map(lambda v: v[0], visited))))

def solve():
    cells = None
    with open("day16_input.txt") as f:
        cells = [
            [Cell(row, col, symbol) for col, symbol in enumerate(line)]
            for row, line in enumerate(f.read().splitlines())
        ]
    possible_starting_beams = [Beam((0, i), DOWN) for i in range(len(cells[0]))] + [Beam((len(cells) - 1, i), UP) for i in range(len(cells[0]))] + [Beam((i, 0), RIGHT) for i in range(len(cells))] + [Beam((i, len(cells) - 1), LEFT) for i in range(len(cells))]

    
    max_result = 0
    for beam in possible_starting_beams:
        count = count_visited(cells, beam)
        if count > max_result:
            max_result = count
    return max_result
print(solve())
