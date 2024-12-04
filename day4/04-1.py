from typing import List


def parse_input(filename) -> str:
    with open(filename, "r") as f:
        lines = f.read()
        return lines


def data_to_matrix(data: str) -> List[List[str]]:
    return [list(line) for line in data.split("\n")]



def find_XMAS_word_in_matrix(matrix: List[List[str]]) -> int:
    occurences = 0
    rows = len(matrix)
    cols = len(matrix[0])
    word = "XMAS"
    
    # Check all 8 directions
    directions = [
        (0,1),   # right
        (0,-1),  # left 
        (1,0),   # down
        (-1,0),  # up
        (1,1),   # diagonal down-right
        (-1,-1), # diagonal up-left
        (1,-1),  # diagonal down-left
        (-1,1)   # diagonal up-right
    ]
    
    for row in range(rows):
        for col in range(cols):
            # Try each direction from current position
            for d_row, d_col in directions:
                found = True
                # Check if word fits in this direction
                for i in range(len(word)):
                    new_row = row + (i * d_row)
                    new_col = col + (i * d_col)
                    
                    if (new_row < 0 or new_row >= rows or 
                        new_col < 0 or new_col >= cols or
                        matrix[new_row][new_col] != word[i]):
                        found = False
                        break
                        
                if found:
                    occurences += 1
                    
    return occurences            


if __name__ == "__main__":
    data = parse_input("04-input.txt")
    matrix = data_to_matrix(data)
    print(find_XMAS_word_in_matrix(matrix))