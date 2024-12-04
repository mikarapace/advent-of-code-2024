from typing import List


# Function to read contents of a file
def read_file(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()


# Function to check if a sequence of numbers meets safety criteria
def calculate_safety_rating(line: List[int]) -> bool:
    # Determine if sequence should be increasing based on first two numbers
    increase = line[0] < line[1]

    # Check each adjacent pair of numbers
    for i in range(len(line) - 1):
        # Check if difference between numbers is between 0 and 4
        if not (0 < abs(line[i] - line[i + 1]) < 4):
            return False
        # If sequence should increase but decreases, fail
        elif increase and line[i] > line[i + 1]:
            return False
        # If sequence should decrease but increases, fail
        elif (not increase) and line[i] < line[i + 1]:
            return False
    return True


# Function to count how many sequences are safe or can be made safe
def calculate_safety_rating_sum(data: str) -> int:
    sum = 0
    # Process each line of input
    for line in data.splitlines():
        # Convert line to list of integers
        line = [int(num) for num in line.split()]
        # Check if sequence is safe as-is
        if calculate_safety_rating(line):
            sum += 1
    return sum


# Main program entry point
if __name__ == "__main__":
    input_file = "02-input.txt"
    data = read_file(input_file)
    print(calculate_safety_rating_sum(data))
