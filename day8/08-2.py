from typing import List, Set
from itertools import combinations


def parse_input(filename: str) -> List[List[str]]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        return [list(line) for line in lines]


def find_antennas(area: List[List[str]]) -> dict:
    antennas = {}
    for y in range(len(area)):
        for x in range(len(area[y])):
            if area[y][x] != ".":
                if antennas.get(area[y][x]) is None:
                    antennas[area[y][x]] = [(x, y)]
                else:
                    antennas[area[y][x]].append((x, y))

    return antennas


def find_antinodes(antennas: dict, border_x: int, border_y: int) -> set:
    antinodes = set()

    for key in antennas.keys():
        list_of_coords = antennas[key]
        coords_combinations = list(combinations(list_of_coords, 2))

        for coords_combination in coords_combinations:
            distance_x, distance_y = (
                coords_combination[0][0] - coords_combination[1][0],
                coords_combination[0][1] - coords_combination[1][1],
            )
            antinode_1_x, antinode_1_y = (
                coords_combination[1][0] - distance_x,
                coords_combination[1][1] - distance_y,
            )
            antinode_2_x, antinode_2_y = (
                coords_combination[0][0] + distance_x,
                coords_combination[0][1] + distance_y,
            )

            antinodes.add((coords_combination[0][0], coords_combination[0][1]))
            antinodes.add((coords_combination[1][0], coords_combination[1][1]))

            while True:
                if 0 <= antinode_1_x < border_x and 0 <= antinode_1_y < border_y:
                    antinodes.add((antinode_1_x, antinode_1_y))
                else:
                    break
                antinode_1_x, antinode_1_y = (
                    antinode_1_x - distance_x,
                    antinode_1_y - distance_y,
                )

            while True:
                if 0 <= antinode_2_x < border_x and 0 <= antinode_2_y < border_y:
                    antinodes.add((antinode_2_x, antinode_2_y))
                else:
                    break
                antinode_2_x, antinode_2_y = (
                    antinode_2_x + distance_x,
                    antinode_2_y + distance_y,
                )

    return antinodes


def print_area(area: List[List[str]], antinodes: Set[tuple]):
    for y in range(len(area)):
        for x in range(len(area[y])):
            if (x, y) in antinodes and area[y][x] == ".":
                area[y][x] = "#"

    for line in area:
        print("".join(line))


if __name__ == "__main__":
    area = parse_input("day8/08-input.txt")
    antennas = find_antennas(area)
    antinodes = find_antinodes(antennas, len(area[0]), len(area))
    print_area(area, antinodes)
    print(f"\nsum of antinodes: {len(antinodes)}")
