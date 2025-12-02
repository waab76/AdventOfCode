import re
from common import get_input_lines

def _is_invalid(id:str):
    check_len = 1
    half = len(id) // 2
    while check_len <= half:
        pattern = r'^(?:' + id[:check_len] + r')+$'
        if re.fullmatch(pattern, id) is not None:
            return True
        check_len += 1

    return False

def main():
    id_ranges = get_input_lines('aoc_02.txt')[0].split(',')
    bad_id_sum = 0

    for id_range in id_ranges:
        start_str, end_str = id_range.split('-')
        current, end = int(start_str), int(end_str)

        while current <= end:
            if _is_invalid(str(current)):
                bad_id_sum += current
            current += 1

    print(f'Sum of invalid ids {bad_id_sum}')

if __name__ == '__main__':
    main()