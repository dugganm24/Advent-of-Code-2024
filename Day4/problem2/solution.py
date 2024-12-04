def parse_word_search(path):
    with open(path, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def count_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    pattern = [
        (-1,-1), (-1,1), # Top M and S 
        (1,-1), (1,1), # Bottom M and S
        (0,0) # Middle A 
    ]
    
    # Check that coordinate is in grid boundaries
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def matches_pattern(center_x, center_y):
       positions = [(center_x + dx, center_y + dy) for dx, dy in pattern]
       
       if not all(is_valid(x, y) for x, y in positions):
           return False
       
       chars = [grid[x][y] for x, y in positions]
       
       diagonal1 = [chars[0], chars[4], chars[3]]
       diagonal2 = [chars[1], chars[4], chars[2]]
       
       return (
           (diagonal1 == ['M', 'A', 'S'] or diagonal1 == ['S', 'A', 'M']) and
           (diagonal2 == ['M', 'A', 'S'] or diagonal2 == ['S', 'A', 'M'])
       )
       
    count = 0
    for r in range(rows):
        for c in range(cols):
            if matches_pattern(r, c):
                count += 1
    return count
       
def main():
    input_file = 'input.txt'
    grid = parse_word_search(input_file)   
    total_occurrences = count_patterns(grid)
    print(total_occurrences)

if __name__ == '__main__':
    main()