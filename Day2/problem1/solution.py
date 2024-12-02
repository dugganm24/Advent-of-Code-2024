
def read_input(path):
    with open(path, 'r') as file:
        reports = [[int(level) for level in line.split()] for line in file if line.strip()]
    return reports

def main():
    
    reports = read_input('input.txt')
    safe_reports = 0

    for report in reports:
        increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report)-1)) 
        decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report)-1))
        
        if increasing or decreasing:
            safe_reports += 1
                
    print(safe_reports)
            
        
if __name__ == "__main__":
    main()