from typing import List


class Guard:
    def __init__(self, x, y, x_border, y_border):
        self.facing = (0, -1)  # up
        self.x = x # horizontal
        self.y = y # vertical
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
            0 <= self.x + self.facing[0] < self.x_border and 0 <= self.y + self.facing[1] < self.y_border
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
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "^":
                return j, i


def calculate_distinct_positions(guard: Guard, matrix: List[List[str]]) -> int:
    blocker = "#"
    positions_visited = set()
    positions_visited.add(f'{guard.x}-{guard.y}')

    while not guard.is_leaving_area():
        x, y = guard.next_position()
        if matrix[y][x] == blocker:
            guard.turn()
            continue
        matrix[guard.y][guard.x] = "X"
        guard.walk()
        matrix[y][x] = "^"
        positions_visited.add(f'{guard.x}-{guard.y}')
    
    for i in range(len(matrix)):
        print(''.join(matrix[i]))

    return len(positions_visited)


if __name__ == "__main__":
    matrix = parse_input("day6/06-input.txt")
    x, y = find_initial_guard_position(matrix)
    distinct_positions_visited = calculate_distinct_positions(Guard(x, y, len(matrix[0]), len(matrix)), matrix)
    print(f"\ndistinct_positions_visited: {distinct_positions_visited}")
