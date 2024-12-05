from collections import defaultdict, deque

def parse_input(path):
    with open(path, 'r') as file:
        lines = file.read().strip().split('\n') #split input into lines 
        divider = lines.index('') #separate rules and updates 
        rules = [tuple(map(int, line.split('|'))) for line in lines[:divider]] #parse rules into tuples
        updates = [list(map(int, line.split(','))) for line in lines[divider+1:]] #parse updates into lists
    return rules, updates

#check if invalid 
def is_invalid(rules, update):
   
    graph = defaultdict(set) #build graph to represent rules
    for x,y in rules:
        graph[x].add(y) #add edges to graph
        
    position = {page: idx for idx, page in enumerate(update)} #position map of pages to their indeces in the update 
    
    #check if any rule is violated
    for x,y in rules:
        if x in position and y in position: 
            if position[x] > position[y]:
                return True
    return False 

#reorder invalid rules through topological sort 
def reorder(rules, update):
    #build graph to represent rules
    #each key is a page, value is a set of pages that must come after it 
    graph = defaultdict(set)
     
    #track in degree (number of incoming edges) for each page 
    #represents how many pages must be processed before current page 
    in_degree = defaultdict(int) 
    
    #convert update list into set for quick lookups
    update_set = set(update) #set of pages in the update
    
    #build graph and in degree map based on rules 
    for x,y in rules:
        #if both pages in rule are part of the update
        if x in update_set and y in update_set:
            graph[x].add(y) #add directed graph edge from x to y 
            in_degree[y] += 1 #increment in degree of y 
            in_degree[x] += 0 #ensure x also in in degree map, prevents issues when processing x later 
    queue = deque([node for node in update if in_degree[node] == 0]) # queue with all pages that have in degree 0, have no dependencies and can be processed first
    sorted_update = [] #initialize sorted update list 
    
    #topological sort using Kahn's algorithm
    while queue:
        current = queue.popleft() #remove page with no dependencies from queue
        sorted_update.append(current) #add to sorted update list
        for neighbor in graph[current]: #for each page that depends on current page
            in_degree[neighbor] -= 1 #decrement in degree of neighbor
            if in_degree[neighbor] == 0: #if neighbor becomes 0, add to queue
                queue.append(neighbor) #means all dependencies have been resolved 
    return sorted_update

def solve(rules, updates):
    invalid_updates = [] 
    
    #loop through updates 
    for update in updates:
        #check if rule is invalid
        if is_invalid(rules, update):
            reordered = reorder(rules, update) #reorder invalid update
            invalid_updates.append(reordered) #append reordered update to invalid updates
    middle_pages = [update[len(update)//2] for update in invalid_updates] #get middle pages of invalid updates
    
    return sum(middle_pages) #sum all middle pages 
    


def main():
    input = 'input.txt'
    rules, updates = parse_input(input)
    result = solve(rules, updates)
    print(result)
    
if __name__ == "__main__":
    main()