from common import get_input_lines
from functools import cache

@cache
def is_possible(design:str, towels:list)->int:
    towel_list = [foo.strip() for foo in towels.split(',')]
    possible = 0
    if len(design) == 0:
        return 1

    for towel in towel_list:
        if design.startswith(towel):
            possible += is_possible(design[len(towel):], towels)

    return possible

def part_1():
    data = get_input_lines('day19.txt')
    towels = data[0]
    designs = data[2:]

    possible = 0
    for design in designs:
        if is_possible(design, towels) > 0:
            possible += 1
    
    print(f'There are {possible} designs possible')
    
def part_2():
    data = get_input_lines('day19.txt')
    towels = data[0]
    designs = data[2:]

    combinations = sum([is_possible(design, towels) for design in designs])
    
    print(f'There are {combinations} combinations possible')

if __name__ == '__main__':
    part_1()
    part_2()