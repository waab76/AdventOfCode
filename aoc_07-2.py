from common import get_input_lines

def calc_possible_values(nums:list)->set:
    if 2 == len(nums):
        return {nums[0] + nums[1], nums[0] * nums[1], int(str(nums[0]) + str(nums[1]))}

    add = list(calc_possible_values([nums[0] + nums[1]] + nums[2:]))
    mult = list(calc_possible_values([nums[0] * nums[1]] + nums[2:]))
    concat = list(calc_possible_values([int(str(nums[0]) + str(nums[1]))] + nums[2:]))

    return set(add + mult + concat)

def main():
    input = get_input_lines('aoc_07.txt')
    calibration_result = 0

    for line in input:
        target = int(line.split()[0][:-1])
        values = [int(x) for x in line.split()[1:]]

        if target in calc_possible_values(values):
            calibration_result += target
    
    print(f'The final calibration result is {calibration_result}')

if __name__ == '__main__':
    main()