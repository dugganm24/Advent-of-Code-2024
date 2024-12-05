from collections import defaultdict, deque

def parse_input(path):
    with open(path, 'r') as file:
        lines = file.read().strip().split('\n') #read input and split into lines 
        divider = lines.index('') #separate rules and updates
        rules = [tuple(map(int, line.split('|'))) for line in lines[:divider]] #parse rules as tuples 
        updates = [list(map(int, line.split(','))) for line in lines[divider+1:]] #parse updates as lists
    return rules, updates

def is_valid(rules, update):
    graph = defaultdict(set) #create a directed graph to represent rules 
    for x,y in rules:
        graph[x].add(y) #add an edge from x to y in the graph
        
    position = {page: idx for idx, page in enumerate(update)} #map pages to their positions
    
    for x,y in rules: #check each rule 
        if x in position and y in position: #only consider rules where both pages are in the update
            if position[x] > position[y]: #if x comes after y, rule is  violated 
                return False
    return True #all rules satisfied 


def solve(rules, updates):
    valid_updates = [] #list to store valid updates 
    for update in updates:
        if is_valid(rules, update):
            valid_updates.append(update) #append update if valid 
    middle_pages = [update[len(update)//2] for update in valid_updates] #extract middle pages 
    
    return sum(middle_pages) #return sum of middle pages
    


def main():
    input = 'input.txt'
    rules, updates = parse_input(input)
    result = solve(rules, updates)
    print(result)
    
    

if __name__ == "__main__":
    main()