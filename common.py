def get_input_lines(filename:str) -> list:
    input = open(filename, 'r')
    return [list(line.strip()) for line in input.readlines()]

def grid_get(grid:list, col: int, row: int, default:str='.') -> str:
    if row < 0 or col < 0:
        return default
    try:
        return grid[row][col]
    except IndexError:
        return default
