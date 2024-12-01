def read_file(filepath: str) -> str:
    """Read content from a file and return it as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def parse_columns(data: str, separator: str = '   ') -> tuple[list[int], list[int]]:
    """
    Parse the input data into two columns of integers.
    
    Args:
        data: String containing the input data
        separator: String used to separate columns (default: '   ')
    
    Returns:
        Tuple containing two lists of integers (left_column, right_column)
    """
    left_column = []
    right_column = []
    
    for line in data.splitlines():
        left, right = line.split(separator)
        left_column.append(int(left))
        right_column.append(int(right))
    
    return left_column, right_column

def calculate_total_distance(left: list[int], right: list[int]) -> int:
    """
    Calculate the total distance between sorted corresponding elements.
    
    Args:
        left: List of integers for the left column
        right: List of integers for the right column
    
    Returns:
        Total distance between corresponding elements
    """
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    
    return sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))

def main():
    """Main function to orchestrate the program flow."""
    input_file = '01-input.txt'
    
    # Read and process the data
    data = read_file(input_file)
    left_column, right_column = parse_columns(data)
    distance = calculate_total_distance(left_column, right_column)
    
    print(distance)

if __name__ == '__main__':
    main()
