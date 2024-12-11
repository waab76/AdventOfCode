from common import get_input_lines_as_grid, grid_get, print_grid
import os

def count_on(grid:list)->int:
    count = 0
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            if '#' == grid[row_idx][col_idx]:
                count += 1
    return count

def neighbors_on(grid:list, row_idx:int, col_idx:int)->int:
    on = 0
    for row_diff in [-1, 0, 1]:
        for col_diff in [-1, 0, 1]:
            if '#' == grid_get(grid, row_idx + row_diff, col_idx + col_diff, '.'):
                on += 1 if not (row_diff == 0 and col_diff == 0) else 0
    return on

def do_update(grid:list)->list:
    new_grid = [['.' for col in range(len(grid[0]))] for row in range(len(grid))]
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            on = neighbors_on(grid, row_idx, col_idx)
            if '#' == grid[row_idx][col_idx] and on in [2,3]:
                new_grid[row_idx][col_idx] = '#'
            elif '.' == grid[row_idx][col_idx] and on == 3:
                new_grid[row_idx][col_idx] = '#'
    new_grid[0][0] = '#'
    new_grid[0][99] = '#'
    new_grid[99][0] = '#'
    new_grid[99][99] = '#'

    return new_grid

def main():
    lights = get_input_lines_as_grid('day18.txt')
    steps = 100

    os.system('clear')
    print_grid(lights)

    for step in range(steps):
        lights = do_update(lights)
        os.system('clear')
        print_grid(lights)
    
    print(f'After {steps} steps, there are {count_on(lights)} lights on')

if __name__ == '__main__':
    main()