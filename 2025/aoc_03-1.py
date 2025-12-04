from common import get_input_lines

def _find_highest(num_array):
    highest, highest_pos = 0, -1
    for check_pos in range(0, len(num_array)):
        if num_array[check_pos] > highest:
            highest = num_array[check_pos]
            highest_pos = check_pos
    print(f'The highest value in {num_array} is {highest} at position {highest_pos}')
    return highest, highest_pos

def _get_max_joltage(bank):
    first_digit, first_pos = _find_highest(bank[:-1])
    second_digit, _ = _find_highest(bank[first_pos + 1:])

    print(f'The max joltage of battery bank {bank} is {first_digit}{second_digit}')
    return 10 * first_digit + second_digit

def main():
    battery_banks = get_input_lines('aoc_03.txt')
    total_joltage = 0

    for bank in battery_banks:
        bank_digits = [int(a) for a in bank]
        total_joltage += _get_max_joltage(bank_digits)

    print(f'Total joltage: {total_joltage}')

if __name__ == '__main__':
    main()