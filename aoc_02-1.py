from common import get_input_lines

def report_safe(report:str, ascending:bool) -> bool:
    levels = [int(data_point) for data_point in report.split()]
    if not ascending:
        levels.reverse()

    is_safe = True
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        is_safe = is_safe and diff >= 1 and diff <= 3
    if is_safe:
        print(f'Report {report} is safe {"ascending" if ascending else "descending"}')
    return is_safe

def main():
    reports = get_input_lines('aoc_02.txt')

    safe_reports = 0

    for report in reports:
        if report_safe(report, True):
            safe_reports += 1
        elif report_safe(report, False):
            safe_reports += 1
    
    print(f'Found {safe_reports} safe reports')

if __name__ == '__main__':
    main()
