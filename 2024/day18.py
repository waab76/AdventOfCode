from common import get_input_lines, grid_get, print_grid
import sys

def get_blocks(count:int)->list:
    lines = get_input_lines('day18.txt')
    blocks = list()

    for idx in range(count):
        parts = list(map(int, lines[idx].split(',')))
        blocks.append((parts[1], parts[0]))
    return blocks

def calc_shortest_path(grid:list, end:tuple)->list:
    steps = [(1,0), (-1,0), (0,1), (0,-1)]
    paths = [[sys.maxsize for col in range(len(grid[0]))] for row in range(len(grid))]
    paths[end[0]][end[1]] = 0
    to_evaluate = list()
    to_evaluate.append(end)

    while len(to_evaluate) > 0:
        curr = to_evaluate.pop(0)
        for step in steps:
            next = (curr[0] + step[0], curr[1] + step[1])
            if grid_get(grid, next[0], next[1], '#') == '#':
                continue
            if paths[next[0]][next[1]] > paths[curr[0]][curr[1]] + 1:
                paths[next[0]][next[1]] = paths[curr[0]][curr[1]] + 1
                to_evaluate.append(next)
    return paths

def part_1():
    grid = [['.' for col in range(71)] for row in range(71)]

    blocks = get_blocks(1024)   

    for block in blocks:
        grid[block[0]][block[1]] = '#'

    paths = calc_shortest_path(grid, (70,70))
    print(f'Shortest path to exit is {paths[0][0]} steps')

    
def part_2():
    pass

if __name__ == '__main__':
    part_1()
    part_2()