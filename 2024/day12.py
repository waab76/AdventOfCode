from common import get_input_lines_as_grid, grid_get

def calc_perimeter(crop:str, grid:list, row:int, col:int)->int:
    contribution = 0
    grid[row][col] = '+'
    for step in ((-1,0),(1,0),(0,-1),(0,1)):
        if not grid_get(grid, row + step[0], col + step[1], '.') in ('+', crop):
            contribution += 1
        elif grid_get(grid, row + step[0], col + step[1]) == crop:
            contribution += calc_perimeter(crop, grid, row + step[0], col + step[1])
    return contribution

def calc_sides(crop:str, grid:list, row:int, col:int)->int:
    corners = 0
    grid[row][col] = '+'
    # Check inside corner
    if not grid_get(grid, row - 1, col) in (crop, '+') and not grid_get(grid, row, col - 1) in (crop, '+'):
        corners += 1
    if not grid_get(grid, row, col - 1) in (crop, '+') and not grid_get(grid, row + 1, col) in (crop, '+'):
        corners += 1
    if not grid_get(grid, row + 1, col) in (crop, '+') and not grid_get(grid, row, col + 1) in (crop, '+'):
        corners += 1
    if not grid_get(grid, row, col + 1) in (crop, '+') and not grid_get(grid, row - 1, col) in (crop, '+'):
        corners += 1
    # Check outside corner
    if grid_get(grid, row - 1, col) in (crop, '+') and grid_get(grid, row, col - 1) in (crop, '+') and not grid_get(grid, row - 1, col - 1) in (crop, '+'):
        corners += 1
    if grid_get(grid, row + 1, col) in (crop, '+') and grid_get(grid, row, col - 1) in (crop, '+') and not grid_get(grid, row + 1, col - 1) in (crop, '+'):
        corners += 1
    if grid_get(grid, row - 1, col) in (crop, '+') and grid_get(grid, row, col + 1) in (crop, '+') and not grid_get(grid, row - 1, col + 1) in (crop, '+'):
        corners += 1
    if grid_get(grid, row + 1, col) in (crop, '+') and grid_get(grid, row, col + 1) in (crop, '+') and not grid_get(grid, row + 1, col + 1) in (crop, '+'):
        corners += 1
    for step in ((-1,0),(1,0),(0,-1),(0,1)):
        if grid_get(grid, row + step[0], col + step[1]) == crop:
            corners += calc_sides(crop, grid, row + step[0], col + step[1])
    return corners

def fill_area(grid:list, row:int, col:int)->int:
    area = 1
    grid[row][col] = '.'
    for step in ((-1,0),(1,0),(0,-1),(0,1)):
        if grid_get(grid, row + step[0], col + step[1], '.') == '+':
            area += fill_area(grid, row + step[0], col + step[1])
    return area

def parse_region(grid:list, row:int, col:int)->tuple:
    crop = grid[row][col]
    perimeter = calc_perimeter(crop, grid, row, col)
    sides = calc_sides(crop, grid, row, col)
    area = fill_area(grid, row, col)
    return (crop, perimeter, area, sides)    

def part_1():
    garden = get_input_lines_as_grid('/home/pi/workspace/AdventOfCode2024/2024/day12.txt')

    regions = list()
    for row in range(len(garden)):
        for col in range(len(garden[row])):
            if not '.' == garden[row][col]:
                region = parse_region(garden, row, col)
                regions.append(region)

    total_cost = 0
    for region in regions:
        print(f'Crop {region[0]}: area {region[1]} perimeter {region[2]} price {region[1] * region[2]}')
        total_cost += region[1] * region[2]

    print(f'Total cost for fencing the garden is {total_cost}')

def part_2():
    garden = get_input_lines_as_grid('/home/pi/workspace/AdventOfCode2024/2024/day12.txt')

    regions = list()
    for row in range(len(garden)):
        for col in range(len(garden[row])):
            if not '.' == garden[row][col]:
                crop = garden[row][col]
                sides = calc_sides(crop, garden, row, col)
                area = fill_area(garden, row, col)
                regions.append((crop, sides, area))

    total_cost = 0
    for region in regions:
        print(f'Crop {region[0]}: area {region[2]} sides {region[1]} price {region[1] * region[2]}')
        total_cost += region[1] * region[2]

    print(f'Total cost for fencing the garden is {total_cost}')

if __name__ == '__main__':
    part_1()
    part_2()