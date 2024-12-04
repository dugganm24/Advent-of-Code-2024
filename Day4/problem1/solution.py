def parse_word_search(path):
    with open(path, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]
    
    # Check that coordinate is in grid boundaries
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # Start at (x,y) and check if word exists in direction (dx,dy)
    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            nx =  x + i * dx
            ny =  y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True
    
    # Loop through all cells in grid
    count = 0
    for r in range(rows):
        for c in range(cols):
            # For each cell, check all directions
            # If word found in that direction, increment count
            for dx, dy in directions:
                if check_direction(r, c, dx, dy):
                    count += 1
    
    return count

def main():
    input_file = 'input.txt'
    
    grid = parse_word_search(input_file)
    
    target_word = "XMAS"
    
    total_occurrences = count_word_occurrences(grid, target_word)
    
    print(total_occurrences)

if __name__ == '__main__':
    main()