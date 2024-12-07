from typing import List
from copy import deepcopy


class Guard:
    def __init__(self, x, y, x_border, y_border):
        self.facing = (0, -1)  # up
        self.x = x  # horizontal
        self.y = y  # vertical
        self.x_border = x_border
        self.y_border = y_border

    def turn(self):
        if self.facing == (0, -1):
            self.facing = (1, 0)  # right
        elif self.facing == (1, 0):
            self.facing = (0, 1)  # down
        elif self.facing == (0, 1):
            self.facing = (-1, 0)  # left
        elif self.facing == (-1, 0):
            self.facing = (0, -1)  # up

    def is_leaving_area(self):
        return not (
            0 <= self.x + self.facing[0] < self.x_border
            and 0 <= self.y + self.facing[1] < self.y_border
        )

    def next_position(self):
        return self.x + self.facing[0], self.y + self.facing[1]

    def walk(self):
        if not self.is_leaving_area():
            self.x += self.facing[0]
            self.y += self.facing[1]


def parse_input(filename: str) -> List[List[str]]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        return [list(line) for line in lines]


def find_initial_guard_position(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[i])):
            if matrix[y][x] == "^":
                return x, y


def is_next_position_paradox_obstruction(
    x: int,
    y: int,
    guard: Guard,  # in starting position
    matrix: List[List[str]],
) -> bool:
    blocker = "#"
    blockers_encountered = set()
    matrix[y][x] = blocker

    while not guard.is_leaving_area():
        x, y = guard.next_position()
        if matrix[y][x] == blocker:
            if f"{x},{y},{guard.x},{guard.y}" in blockers_encountered:
                return True
            else:
                blockers_encountered.add(f"{x},{y},{guard.x},{guard.y}")
            guard.turn()
            continue
        guard.walk()

    return False


def calculate_distinct_positions(guard: Guard, matrix: List[List[str]]) -> int:
    starting_position_guard = deepcopy(guard)
    paradox_obstructions = set()

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if x == starting_position_guard.x and y == starting_position_guard.y:
                continue
            if matrix[y][x] != "#" and is_next_position_paradox_obstruction(
                x,
                y,
                deepcopy(starting_position_guard),
                deepcopy(matrix),
            ):
                paradox_obstructions.add(f"{x},{y}")
                matrix[y][x] = "0"

    print("\n")
    for i in range(len(matrix)):
        print("".join(matrix[i]))

    return len(paradox_obstructions)


if __name__ == "__main__":
    matrix = parse_input("day6/06-input.txt")
    x, y = find_initial_guard_position(matrix)
    paradox_obstructions = calculate_distinct_positions(
        Guard(x, y, len(matrix[0]), len(matrix)), matrix
    )
    print(f"\nparadox_obstructions: {paradox_obstructions}")
