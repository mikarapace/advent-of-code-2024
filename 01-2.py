from collections import Counter
from typing import List

def read_file(filepath: str) -> str:
    """Read and return the contents of a file."""
    with open(filepath, 'r') as file:
        return file.read()

def parse_columns(data: str, separator: str = '   ') -> tuple[List[int], List[int]]:
    """
    Parse input data into two columns of numbers.
    
    Args:
        data: String containing the input data
        separator: String used to separate columns
    
    Returns:
        Tuple of (left_column, right_column) lists
    """
    left_column, right_column = [], []
    
    for line in data.splitlines():
        left, right = line.split(separator)
        left_column.append(int(left))
        right_column.append(int(right))
    
    return left_column, right_column

def calculate_similarity_score(left: List[int], right: List[int]) -> int:
    """
    Calculate similarity score based on matching numbers between columns.
    For each number in left column, multiply it by its frequency in right column.
    
    Args:
        left: List of numbers from left column
        right: List of numbers from right column
    
    Returns:
        Total similarity score
    """
    # Create a Counter of right column for O(1) lookup
    right_counts = Counter(right)
    
    # Calculate similarity score using dictionary comprehension
    similarity_map = {
        num: num * right_counts[num] 
        for num in set(left)
    }
    
    return sum(similarity_map[num] for num in left)

def main() -> None:
    """Main function to process input and calculate similarity score."""
    input_file = '01-input.txt'
    
    # Process input data
    data = read_file(input_file)
    left_column, right_column = parse_columns(data)
    
    # Calculate and print result
    similarity_score = calculate_similarity_score(left_column, right_column)
    print(similarity_score)

if __name__ == '__main__':
    main()
