from common import get_input_lines

def _find_highest(num_array:list[int]):
    if not isinstance(num_array, list):
        return num_array
    
    highest, highest_pos = 0, -1
    for check_pos in range(0, len(num_array)):
        if num_array[check_pos] > highest:
            highest = num_array[check_pos]
            highest_pos = check_pos
    return highest, highest_pos

def _get_max_joltage(bank:list[int], digits:int) -> int:
    remaining_digits = digits - 1

    if remaining_digits > 0:
        max_value, max_pos = _find_highest(bank[:(remaining_digits * -1)])
        return max_value * (10 ** remaining_digits) + _get_max_joltage(bank[max_pos + 1:], remaining_digits)
    else:
        highest, _ = _find_highest(bank)
        return highest

def main():
    battery_banks = get_input_lines('aoc_03.txt')
    total_joltage = 0

    for bank in battery_banks:
        bank_digits = [int(a) for a in bank]
        total_joltage += _get_max_joltage(bank_digits, 12)

    print(f'Total joltage: {total_joltage}')

if __name__ == '__main__':
    main()