import re
from typing import List

def parse_input(filename) -> str:
    with open(filename, 'r') as f:
        lines = f.read()
        return lines

def find_multiplications_in_line(line: str) -> List[tuple[int,int]]:
    # find all substrings like mul(X, Y) where X and Y are numbers
    return re.findall(r'mul\((\d+),(\d+)\)', line)

def find_dont_multiplications_in_line(line: str) -> List[tuple[int,int]]:
    # find text between "don't() and do()"
    text_between_dont_and_do_list = re.findall(r'don\'t\(\)(.*?)do\(\)', line)
    result = list()
    for text in text_between_dont_and_do_list:
        # find multiplications in these substrings
        result = result + find_multiplications_in_line(text)
    return result

if __name__ == '__main__':
    data = parse_input('03-input.txt')
    # find all substrings like mul(X, Y) where X and Y are numbers
    # and return list of tuples (X, Y)
    multiplications = find_multiplications_in_line(data)
    # filter out multiplications to substract
    dont_multiplications = find_dont_multiplications_in_line(data)
    # convert list of tuples to list of lists
    multiplications = [[int(x), int(y)] for x, y in multiplications]
    dont_multiplications = [[int(x), int(y)] for x, y in dont_multiplications]
    # multiply X and Y
    multiplications = [x * y for x, y in multiplications]
    dont_multiplications = [x * y for x, y in dont_multiplications]
    # sum all multiplications and remove "don't()" multiplications
    print(sum(multiplications) - sum(dont_multiplications))
