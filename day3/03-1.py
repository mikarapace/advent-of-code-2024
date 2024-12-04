import re
from typing import List

def parse_input(filename) -> str:
    with open(filename, 'r') as f:
        lines = f.read()
        return lines

def find_multiplications_in_line(line: str) -> List[tuple[int,int]]:
    # find all substrings like mul(X, Y) where X and Y are numbers
    return re.findall(r'mul\((\d+),(\d+)\)', line)

if __name__ == '__main__':
    data = parse_input('03-input.txt')
    # find all substrings like mul(X, Y) where X and Y are numbers
    # and return list of tuples (X, Y)
    multiplications = find_multiplications_in_line(data)
    # convert list of tuples to list of lists
    multiplications = [[int(x), int(y)] for x, y in multiplications]
    # multiply X and Y
    multiplications = [x * y for x, y in multiplications]
    # sum all multiplications
    print(sum(multiplications))
