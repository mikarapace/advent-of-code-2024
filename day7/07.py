import operator
from typing import List
import itertools


def parse_input(filename: str) -> dict:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        equations = dict()
        for line in lines:
            test_value = line.split(": ")[0]
            numbers = line.split(": ")[1].split(" ")
            equations[int(test_value)] = [int(x) for x in numbers]
        return equations


def is_equation_valid(test_value: int, numbers: List[int], operators: List) -> bool:
    for operator_combination in itertools.product(operators, repeat=len(numbers) - 1):
        result = numbers[0]
        for index in range(len(operator_combination)):
            result = operator_combination[index](result, numbers[index+1])
        if result == test_value:
            return True

    return False

def calculate_total_calibration_result(equations, operators) -> int:
    total_calibration_result = 0
    for key in equations.keys():
        if (is_equation_valid(key, equations[key], operators)):
            total_calibration_result += key
    return total_calibration_result

if __name__ == "__main__":
    equations = parse_input("day7/07-input.txt")
    operators = [operator.add, operator.mul]
    part1_total_calibration_result = calculate_total_calibration_result(equations, operators)
    print(f"part 1 total_calibration_result: {part1_total_calibration_result}")
    operators = [operator.add, operator.mul, lambda x, y: int("".join([str(x), str(y)]))]
    part2_total_calibration_result = calculate_total_calibration_result(equations, operators)
    print(f"part 2 total_calibration_result: {part2_total_calibration_result}")

