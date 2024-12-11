def get_input_lines(filename:str) -> list:
    input = open(filename, 'r')
    return [line.strip() for line in input.readlines()]

def get_input_lines_as_grid(filename:str) -> list:
    input = open(filename, 'r')
    return [list(line.strip()) for line in input.readlines()]

def grid_get(grid:list, row: int, col: int, default:str='.') -> str:
    if row < 0 or col < 0:
        return default
    try:
        return grid[row][col]
    except IndexError:
        return default

def print_grid(grid:list):
    for row in grid:
        print(''.join(row))