from common import get_input_lines

def get_move(dir:str)->tuple:
    moves = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    return moves[dir]

def attempt_move(grid:list, pos:tuple, dir:str)->tuple:
    mov = get_move(dir)
    next_pos = (pos[0] + mov[0], pos[1] + mov[1])
    if '#' == grid[next_pos[0]][next_pos[1]]:
        return (False, pos)
    elif 'O' == grid[next_pos[0]][next_pos[1]]:
        if attempt_move(grid, next_pos, dir)[0]:
            grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = '.'
            return (True, next_pos)
        else:
            return (False, pos)
    else:
        grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = '.'
        return (True, next_pos)
    
def parse_input_file():
    input = get_input_lines('day15.txt')
    map = list()
    robot = tuple()
    moves = list()

    for row in range(len(input)):
        if '#' in input[row]:
            map.append(list(input[row]))
            if '@' in input[row]:
                robot = (row, input[row].index('@'))
        elif len(input[row]) > 0 and input[row][0] in '^v<>':
            moves += list(input[row])

    return map, robot, moves

def part_1():
    map, robot, moves = parse_input_file()
    
    print(f'Robot starts at {robot}')

    for move in moves:
        (success, robot) = attempt_move(map, robot, move)

    gps_sum = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            gps_sum += 100 * row + col if map[row][col] == 'O' else 0
    print(f'Sum of box GPS is {gps_sum}')

def double_map(map:list)->list:
    new_map = list()
    for row in map:
        new_row = list()
        for item in row:
            if item == '#':
                new_row += ['#','#']
            elif item == '.':
                new_row += ['.','.']
            elif item == 'O':
                new_row += ['[',']']
            else:
                new_row += ['@','.']
        new_map.append(new_row)
    return new_map

def can_move(grid:list, pos:tuple, dir:str)->bool:
    mov = get_move(dir)
    next_pos = (pos[0] + mov[0], pos[1] + mov[1])
    if '#' == grid[next_pos[0]][next_pos[1]]:
        return False
    elif '.' == grid[next_pos[0]][next_pos[1]]:
        return True
    elif dir in '<>':
        return can_move(grid, next_pos, dir)
    else:
        if '[' == grid[next_pos[0]][next_pos[1]]:
            other_half = (next_pos[0], next_pos[1] + 1)
            return can_move(grid, next_pos, dir) and can_move(grid, other_half, dir)
        else:
            other_half = (next_pos[0], next_pos[1] - 1)
            return can_move(grid, next_pos, dir) and can_move(grid, other_half, dir)

def do_move(grid:list, pos:tuple, dir:str)->tuple:
    mov = get_move(dir)
    next_pos = (pos[0] + mov[0], pos[1] + mov[1])
    if '#' == grid[next_pos[0]][next_pos[1]]:
        return pos
    elif '.' == grid[next_pos[0]][next_pos[1]]:
        grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = '.'
        return next_pos
    elif dir in '<>':
        do_move(grid, next_pos, dir)
        grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = '.'
        return next_pos
    else:
        other_half = tuple()
        if '[' == grid[next_pos[0]][next_pos[1]]:
            other_half = (next_pos[0], next_pos[1] + 1)
        else:
            other_half = (next_pos[0], next_pos[1] - 1)
        do_move(grid, next_pos, dir)
        do_move(grid, other_half, dir)
        grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = '.'
        return next_pos
    
def part_2():
    map, robot, moves = parse_input_file()
    map = double_map(map)
    robot = (robot[0], 2 * robot[1])

    for move in moves:
        if can_move(map, robot, move):
            robot = do_move(map, robot, move)

    gps_sum = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            gps_sum += 100 * row + col if map[row][col] == '[' else 0
    print(f'Sum of box GPS is {gps_sum}')

if __name__ == '__main__':
    part_1()
    part_2()