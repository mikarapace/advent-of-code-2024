from typing import List


def parse_input(filename) -> str:
    with open(filename, "r") as f:
        lines = f.read()
        return lines


def data_to_matrix(data: str) -> List[List[str]]:
    return [list(line) for line in data.split("\n")]


def find_X_MAS_word_in_matrix(matrix: List[List[str]]) -> int:
    occurences = 0
    rows = len(matrix)
    cols = len(matrix[0])

    # Check all 8 directions
    directions = [
        (1,1),   # diagonal down-right
        (-1,-1), # diagonal up-left
        (1,-1),  # diagonal down-left
        (-1,1)   # diagonal up-right
    ]

    for row in range(rows):
        for col in range(cols):
            # Start from a letter A
            if matrix[row][col] != "A":
                continue

            mas_found = 0
            # Try each direction from current position to find M and S letters
            for d_row, d_col in directions:
                row_before = row - d_row
                col_before = col - d_col

                row_after = row + d_row
                col_after = col + d_col

                if (
                    0 <= row_before < rows
                    and 0 <= col_before < cols
                    and 0 <= row_after < rows
                    and 0 <= col_after < cols
                    and matrix[row_before][col_before] == "M" and matrix[row_after][col_after] == "S"
                ):
                    mas_found += 1

                # Find MAS word twice to validate an occurence
                if mas_found >= 2:
                    occurences += 1
                    break

    return occurences


if __name__ == "__main__":
    data = parse_input("04-input.txt")
    matrix = data_to_matrix(data)
    print(find_X_MAS_word_in_matrix(matrix))
