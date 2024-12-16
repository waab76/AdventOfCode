from common import get_input_lines_as_grid, print_grid
import sys

def calc_shortest_paths(grid:list, start:tuple)->list:
    steps = [(1,0), (-1,0), (0,1), (0,-1)]
    paths = [[sys.maxsize for col in range(len(grid[0]))] for row in range(len(grid))]
    paths[start[0]][start[1]] = 0
    to_evaluate = list()

    for step in steps:
        if not '#' == grid[start[0] + step[0]][start[1] + step[1]]:
            to_evaluate.append(((start[0] + step[0], start[1] + step[1]), step))
            if (0,1) == step:
                paths[start[0] + step[0]][start[1] + step[1]] = 1
            else:
                paths[start[0] + step[0]][start[1] + step[1]] = 1001
            grid[start[0] + step[0]][start[1] + step[1]] = '+'

    while len(to_evaluate) > 0:
        # print_grid(grid)
        eval = to_evaluate.pop(0)
        curr = eval[0]
        for step in steps:
            next = (curr[0] + step[0], curr[1] + step[1])
            if grid[next[0]][next[1]] in ['S', '#']:
                continue
            diff = 1001 # assume turn and move
            if step == eval[1]: # moving in the same direction
                diff = 1
            if paths[next[0]][next[1]] > paths[curr[0]][curr[1]] + diff:
                paths[next[0]][next[1]] = paths[curr[0]][curr[1]] + diff
                grid[next[0]][next[1]] = '+'
                to_evaluate.append((next, step))

    return paths

def part_1():
    maze = get_input_lines_as_grid('day16.txt')
    start, end = tuple(), tuple()

    for row_idx in range(len(maze)):
        if 'E' in maze[row_idx]:
            end = (row_idx, maze[row_idx].index('E'))
        if 'S' in maze[row_idx]:
            start = (row_idx, maze[row_idx].index('S'))
    
    path_lengths = calc_shortest_paths(maze, start)
    # 72392 is too low
    print(f'Shortest path score is {path_lengths[end[0]][end[1]]}')
    
def part_2():
    pass

if __name__ == '__main__':
    part_1()
    part_2()