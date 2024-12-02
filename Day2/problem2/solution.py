def read_input(path):
    with open(path, 'r') as file:
        reports = [[int(level) for level in line.split()] for line in file if line.strip()]
    return reports

def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def main():
    reports = read_input('input.txt')
    safe_reports = 0

    for report in reports:
        if is_safe(report):
            safe_reports += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe_reports += 1
                break  

    print(safe_reports)

if __name__ == "__main__":
    main()