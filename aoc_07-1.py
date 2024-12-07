from common import get_input_lines

def calc_possible_values(nums:list)->set:
    if 2 == len(nums):
        poss = {nums[0] + nums[1], nums[0] * nums[1]}
        #print(f'Possible values are: {poss}')
        return poss
    
    last = nums[-1]
    other_poss = calc_possible_values(nums[:-1])

    adds = [last + x for x in other_poss]
    #print(f'{last} + {other_poss} => {adds}')
    mults = [last * x for x in other_poss]
    #print(f'{last} * {other_poss} => {mults}')

    return set(adds + mults)


def main():
    input = get_input_lines('aoc_07.txt')
    calibration_result = 0

    for line in input:
        target = int(line.split()[0][:-1])
        values = [int(x) for x in line.split()[1:]]

        #print(f'Can {target} be produced from {values}?')
        poss_vals = calc_possible_values(values)

        if target in poss_vals:
            #print(f'{target} IS in {poss_vals}')
            calibration_result += target
        #else:
        #    print(f'{target} IS NOT in {poss_vals}')
    
    # 40212532 is too low
    print(f'The final calibration result is {calibration_result}')

if __name__ == '__main__':
    main()