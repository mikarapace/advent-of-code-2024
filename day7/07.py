import operator
from typing import List
import itertools



class Equation:
    def __init__(self, test_value, numbers, operators):
        self.test_value: int = test_value
        self.numbers: List[int] = numbers
        self.operators: List[function] = operators

    def __str__(self):
        return f"test_value: {self.test_value} | numbers: {self.numbers} | operators: {self.operators}"

    def is_equation_valid(self) -> bool:
        operator_combinations = itertools.product(
            self.operators, repeat=len(self.numbers) - 1
        )
        for operator_combination in operator_combinations:
            result = self.numbers[0]
            for index in range(len(operator_combination)):
                result = operator_combination[index](result, self.numbers[index + 1])
                if result > self.test_value:
                    break
            if result == self.test_value:
                return True

        return False
    
    def is_equation_valid_recursive(self, remaining_numbers = list(), current_result = 0) -> bool:
        if current_result == 0:
            remaining_numbers = self.numbers.copy()
            current_result = remaining_numbers[0]
            remaining_numbers.pop(0)
        
        if current_result > self.test_value:
            return False
        
        if not remaining_numbers:
            return self.test_value == current_result
        
        previous_result = current_result
        previous_numbers = remaining_numbers
        for operator in self.operators:
            current_result = operator(current_result, remaining_numbers[0])
            remaining_numbers = remaining_numbers.copy()
            remaining_numbers.pop(0)
            if self.is_equation_valid_recursive(remaining_numbers, current_result):
                return True
            else:
                current_result = previous_result
                remaining_numbers = previous_numbers
        
        return False


def parse_input(filename: str, operators: List) -> List[Equation]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        equations = list()
        for line in lines:
            test_value = line.split(": ")[0]
            numbers = line.split(": ")[1].split(" ")
            equations.append(
                Equation(int(test_value), [int(x) for x in numbers], operators)
            )
        return equations


def calculate_total_calibration_result(equations: List[Equation]) -> int:
    total_calibration_result = 0
    for equation in equations:
        # print(equation)
        if equation.is_equation_valid_recursive():
            total_calibration_result += equation.test_value
    return total_calibration_result


if __name__ == "__main__":
    input_file = "day7/07-input.txt"
    operators = [operator.add, operator.mul]
    equations = parse_input(input_file, operators)
    part1_total_calibration_result = calculate_total_calibration_result(equations)
    print(f"part 1 total_calibration_result: {part1_total_calibration_result}")
    operators = [
        operator.add,
        operator.mul,
        lambda x, y: int("".join([str(x), str(y)])),
    ]
    equations = parse_input(input_file, operators)
    part2_total_calibration_result = calculate_total_calibration_result(equations)
    print(f"part 2 total_calibration_result: {part2_total_calibration_result}")
