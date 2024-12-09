def get_input_lines(filename:str) -> list:
    input = open(filename, 'r')
    return [line.strip() for line in input.readlines()]

def get_input_lines_as_grid(filename:str) -> list:
    input = open(filename, 'r')
    return [list(line.strip()) for line in input.readlines()]

def grid_get(grid:list, col: int, row: int, default:str='.') -> str:
    if row < 0 or col < 0:
        return default
    try:
        return grid[row][col]
    except IndexError:
        return default

def print_list(data:list, limit:int=80):
    printable = ''
    for item in data:
        printable += str(item)
        if len(printable) > limit:
            break
    print(printable)