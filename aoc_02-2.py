from common import get_input_lines

def report_safe(levels:list) -> bool:
    is_safe = True
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        is_safe = is_safe and diff >= 1 and diff <= 3
    if is_safe:
        print(f'Report {levels} is safe')
    return is_safe

def main():
    reports = get_input_lines('aoc_02.txt')

    safe_reports = 0

    for report in reports:
        levels = [int(data_point) for data_point in report.split()]
        if report_safe(levels):
            safe_reports += 1
            continue

        for i in range(len(levels)):
            removed = levels.pop(i)
            if report_safe(levels):
                safe_reports += 1
                break
            levels.insert(i, removed)
        
        levels.reverse()
        if report_safe(levels):
            safe_reports += 1
            continue

        for i in range(len(levels)):
            removed = levels.pop(i)
            if report_safe(levels):
                safe_reports += 1
                break
            levels.insert(i, removed)
    
    print(f'Found {safe_reports} safe reports')

if __name__ == '__main__':
    main()
