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
    
    similarity_score = 0 
    
    freq = {}
    
    for num in right:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1


    for num in left:
        if num in freq:
            similarity_score += (num * freq[num])
                
    print(similarity_score)        
    
    
if __name__ == "__main__":
    main()