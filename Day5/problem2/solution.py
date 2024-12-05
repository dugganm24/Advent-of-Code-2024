from collections import defaultdict, deque

def parse_input(path):
    with open(path, 'r') as file:
        lines = file.read().strip().split('\n') 
        divider = lines.index('') 
        rules = [tuple(map(int, line.split('|'))) for line in lines[:divider]] 
        updates = [list(map(int, line.split(','))) for line in lines[divider+1:]] 
    return rules, updates

def is_invalid(rules, update):
    graph = defaultdict(set) 
    for x,y in rules:
        graph[x].add(y) 
        
    position = {page: idx for idx, page in enumerate(update)} 
    
    for x,y in rules:
        if x in position and y in position: 
            if position[x] > position[y]:
                return True
    return False 

def reorder(rules, update):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    update_set = set(update)
    
    for x,y in rules:
        if x in update_set and y in update_set:
            graph[x].add(y)
            in_degree[y] += 1
            in_degree[x] += 0
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update

def solve(rules, updates):
    invalid_updates = [] 
    for update in updates:
        if is_invalid(rules, update):
            reordered = reorder(rules, update)
            invalid_updates.append(reordered)
    middle_pages = [update[len(update)//2] for update in invalid_updates] 
    
    return sum(middle_pages) 
    


def main():
    input = 'input.txt'
    rules, updates = parse_input(input)
    result = solve(rules, updates)
    print(result)
    
if __name__ == "__main__":
    main()