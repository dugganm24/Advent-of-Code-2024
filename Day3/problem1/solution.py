import re

def parse_input(path):
    with open(path, 'r') as file:
        content = file.read().strip()
        return content

def main():
    input_text = parse_input('input.txt')  
    total = 0

    pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'

    matches = re.findall(pattern, input_text)
    
    for digit1, digit2 in matches:
        total += int(digit1) * int(digit2)

    print(f'Total: {total}')

if __name__ == '__main__':
    main()
