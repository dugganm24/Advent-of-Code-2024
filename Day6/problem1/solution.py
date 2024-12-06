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
        '^': (-1, 0), # up
        'v': (1, 0), # down
        '<': (0, -1), # left
        '>': (0, 1) # right
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
        visited.add(pos)
        r, c = pos
        dr, dc = DIRECTIONS[direction]
        nr, nc = r + dr, c + dc
        
        if not (0 <= nr < rows and 0 <= nc < cols):
            break
        
        if grid[nr][nc] == '#':
            direction = RIGHT_TURN[direction]
        else:
            pos = (nr, nc)
    return len(visited)

def main():
    path = 'input.txt'
    grid, start_pos, start_dir = parse_input(path)
    positions = simulate_guard(grid, start_pos, start_dir)
    print(positions)
    
if __name__ == '__main__':
    main()