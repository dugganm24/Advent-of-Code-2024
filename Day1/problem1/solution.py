
def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def main():
    
    input_lines = read_input('input.txt')

    parsed_numbers = [[int(num) for num in line.split()] for line in input_lines]
    
    left = [nums[0] for nums in parsed_numbers]
    right = [nums[1] for nums in parsed_numbers]
    
    left.sort()
    right.sort()
    
    distance = sum(abs(l-r) for l, r in zip(left, right))
    
    print("distance: ", distance)
            
        
if __name__ == "__main__":
    main()