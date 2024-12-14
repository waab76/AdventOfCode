from common import get_input_lines
import re, sys

def tokens_for_prize(a_button:tuple, b_button:tuple, prize_loc:tuple)->int:
    a = round((prize_loc[1] - ((b_button[1] * prize_loc[0]) / b_button[0])) / (a_button[1] - ((b_button[1] * a_button[0]) / b_button[0])))
    b = round((prize_loc[0] - a_button[0] * a) / b_button[0])

    if (a * a_button[0] + b * b_button[0], a * a_button[1] + b * b_button[1]) == prize_loc:
        return a * 3 + b

    return 0

def part_1():
    machines = get_input_lines('day13.txt')

    total_tokens = 0

    for machine in range(0, len(machines), 4):
        a_match = re.match(r'Button A: X\+(\d+), Y\+(\d+)', machines[machine])
        a_button = (int(a_match.group(1)), int(a_match.group(2)))
        b_match = re.match(r'Button B: X\+(\d+), Y\+(\d+)', machines[machine+1])
        b_button = (int(b_match.group(1)), int(b_match.group(2)))
        prize_match = re.match(r'Prize: X=(\d+), Y=(\d+)', machines[machine+2])
        prize_loc = (int(prize_match.group(1)), int(prize_match.group(2)))
        print(f'Machine {machine + 1}')
        total_tokens += tokens_for_prize(a_button, b_button, prize_loc)
    
    print(f'Part 1: Spent {total_tokens} to win all prizes')

def part_2():
    machines = get_input_lines('day13.txt')

    total_tokens = 0

    for machine in range(0, len(machines), 4):
        a_match = re.match(r'Button A: X\+(\d+), Y\+(\d+)', machines[machine])
        a_button = (int(a_match.group(1)), int(a_match.group(2)))
        b_match = re.match(r'Button B: X\+(\d+), Y\+(\d+)', machines[machine+1])
        b_button = (int(b_match.group(1)), int(b_match.group(2)))
        prize_match = re.match(r'Prize: X=(\d+), Y=(\d+)', machines[machine+2])
        prize_loc = (int(prize_match.group(1)) + 10000000000000, int(prize_match.group(2)) + 10000000000000)
        print(f'Machine {machine + 1}')
        total_tokens += tokens_for_prize(a_button, b_button, prize_loc)
    
    print(f'Part 2: Spent {total_tokens} to win all prizes')

if __name__ == '__main__':
    part_1()
    part_2()