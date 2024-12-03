import re

def parse_input(path):
    with open(path, 'r') as file:
        content = file.read().strip()
        return content

def main():
    input_text = parse_input('input.txt')  
    total = 0
    enabled = True  

    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, input_text)
    
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            if enabled:
                digit1, digit2 = re.findall(r'\d+', match)
                total += int(digit1) * int(digit2)
                
    print(f"Final Total: {total}")

if __name__ == '__main__':
    main()