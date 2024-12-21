from common import get_input_lines
from functools import cache
from itertools import permutations

num_pad = {'7':(0,0), '8':(0,1), '9':(0,2),
            '4':(1,0), '5':(1,1), '6':(1,2),
            '1':(2,0), '2':(2,1), '3':(2,2),
            ' ':(3,0), '0':(3,1), 'A':(3,2)}

dir_pad = {' ':(0,0), '^':(0,1), 'A':(0,2),
            '<':(1,0), 'v':(1,1), '>':(1,2)}

dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

@cache
def get_shortest_command_len(bot_num, curr_key, dest_key, bot_count)->int:
    pad = num_pad if bot_num == 0 else dir_pad
    curr = pad[curr_key]
    dest = pad[dest_key]
    row_diff, col_diff = dest[0] - curr[0], dest[1] - curr[1]
    if bot_num == bot_count - 1:
        return abs(row_diff) + abs(col_diff) + 1
    
    if row_diff == 0 and col_diff == 0:
        return 1
    
    moves = []
    for _ in range(abs(row_diff)):
        moves.append('^' if row_diff < 0 else 'v')
    for _ in range(abs(col_diff)):
        moves.append('<' if col_diff < 0 else '>')

    candidates = []
    for r in set(permutations(moves)):
        pos = curr
        steps = 0
        for i, dir_key in enumerate(r):
            steps += get_shortest_command_len(bot_num + 1, 'A' if i == 0 else r[i - 1], dir_key, bot_count)
            pos = (pos[0] + dirs[dir_key][0], pos[1] + dirs[dir_key][1])
            if pos == pad[' ']:
                break
        else:
            steps += get_shortest_command_len(bot_num + 1, r[-1], 'A', bot_count)
            candidates.append(steps)
    return min(candidates)

def part_1():
    codes = ['985A', '540A', '463A', '671A', '382A']

    tot_complexity = 0
    for code in codes:
        command_len = get_shortest_command_len(0, 'A', code[0], 3)
        for i in range(1, len(code)):
            command_len += get_shortest_command_len(0, code[i - 1], code[i], 3)
        tot_complexity += command_len * int(code[:-1])

    print(f'Total complexity is {tot_complexity}')
    
def part_2():
    codes = ['985A', '540A', '463A', '671A', '382A']

    tot_complexity = 0
    for code in codes:
        command_len = get_shortest_command_len(0, 'A', code[0], 26)
        for i in range(1, len(code)):
            command_len += get_shortest_command_len(0, code[i - 1], code[i], 26)
        tot_complexity += command_len * int(code[:-1])

    print(f'Total complexity is {tot_complexity}')

if __name__ == '__main__':
    part_1()
    part_2()