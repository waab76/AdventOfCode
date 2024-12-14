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
    area = fill_area(grid, row, col)
    return (crop, perimeter, area)    

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

if __name__ == '__main__':
    part_1()