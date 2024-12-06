def parse_input(path):
    with open(path, 'r') as file:
        input_lines = [line.strip() for line in file if line.strip()]
    
    grid = [list(line) for line in input_lines]
    start_pos = None
    start_dir = None

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in ['^', 'v', '<', '>']:
                start_pos = (r, c)
                start_dir = cell
                break
        if start_pos:
            break
    
    return grid, start_pos, start_dir


def simulate_guard(grid, start_pos, start_dir):
    DIRECTIONS = {
        '^': (-1, 0),  # Up
        'v': (1, 0),   # Down
        '<': (0, -1),  # Left
        '>': (0, 1)    # Right
    }
    RIGHT_TURN = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }
    visited = set()
    pos = start_pos
    direction = start_dir
    rows = len(grid)
    cols = len(grid[0])
    
    while True:
        if (pos, direction) in visited:
            return True  # Loop detected
        visited.add((pos, direction))
        
        r, c = pos
        dr, dc = DIRECTIONS[direction]
        nr, nc = r + dr, c + dc
        
        # Check bounds
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False  # Guard exits the grid
        
        if grid[nr][nc] == '#':
            direction = RIGHT_TURN[direction]
        else:
            pos = (nr, nc)


def count_valid_obstructions(grid, start_pos, start_dir):
    rows = len(grid)
    cols = len(grid[0])
    valid_positions = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) != start_pos and grid[r][c] == '.':
                # Temporarily place an obstruction
                grid[r][c] = '#'
                if simulate_guard(grid, start_pos, start_dir):
                    valid_positions += 1
                # Remove the obstruction
                grid[r][c] = '.'
    
    return valid_positions


def main():
    path = 'input.txt'
    grid, start_pos, start_dir = parse_input(path)
    result = count_valid_obstructions(grid, start_pos, start_dir)
    print("Number of valid obstruction positions:", result)


if __name__ == '__main__':
    main()