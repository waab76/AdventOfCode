from common import get_input_lines_as_grid, grid_get, print_grid
from datetime import datetime

def calc_path_dist(grid:list, start:tuple)->list:
    steps = [(1,0), (-1,0), (0,1), (0,-1)]
    paths = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    paths[start[0]][start[1]] = 1
    to_evaluate = list()
    to_evaluate.append(start)

    while len(to_evaluate) > 0:
        curr = to_evaluate.pop(0)
        for step in steps:
            next = (curr[0] + step[0], curr[1] + step[1])
            if grid_get(grid, next[0], next[1], '#') == '#':
                continue
            if paths[next[0]][next[1]] == 0:
                paths[next[0]][next[1]] = paths[curr[0]][curr[1]] + 1
                to_evaluate.append(next)
    return paths

def get_cheats(track_positions:list, distances:list, max_dist:int, min_val:int)->set:
    cheats = set()
    for cheat_start in track_positions:
        for cheat_end in track_positions:
            cheat_dist = abs(cheat_end[0] - cheat_start[0]) + abs(cheat_end[1] - cheat_start[1])
            cheat_val = distances[cheat_end[0]][cheat_end[1]] - distances[cheat_start[0]][cheat_start[1]] - cheat_dist
            if  cheat_dist <= max_dist:
                if cheat_val >= min_val:
                    # print(f'Valid cheat from {cheat_start} to {cheat_end} worth {cheat_val}')
                    cheats.add((cheat_start, cheat_end))
    return cheats

def part_1():
    track = get_input_lines_as_grid('day20.txt')
    start, cheat_starts = tuple(), list()
    cheat_moves = [(0,-2), (-1,-1), (-2,0), (-1,1), (0,2), (1,1), (2,0), (1,-1)]

    for row_idx in range(len(track)):
        for col_idx in range(len(track[row_idx])):
            if not '#' ==  track[row_idx][col_idx]:
                cheat_starts.append((row_idx, col_idx))
            if 'S' == track[row_idx][col_idx]:
                start = (row_idx, col_idx)

    dist = calc_path_dist(track, start)

    cheats = list()
    for cheat_start in cheat_starts:
        for cheat_move in cheat_moves:
            cheat_end = (cheat_start[0] + cheat_move[0], cheat_start[1] + cheat_move[1])
            if not '#' == grid_get(track, cheat_end[0], cheat_end[1], '#'):
                cheat_value = dist[cheat_end[0]][cheat_end[1]] - dist[cheat_start[0]][cheat_start[1]] - 2
                if cheat_value >= 100:
                    cheats.append((cheat_start, cheat_move, cheat_value))

    print(f'There are {len(cheats)} cheats available')
    
def part_2():
    track = get_input_lines_as_grid('day20.txt')
    start, track_positions = tuple(), list()

    for row_idx in range(len(track)):
        for col_idx in range(len(track[row_idx])):
            if not '#' ==  track[row_idx][col_idx]:
                track_positions.append((row_idx, col_idx))
            if 'S' == track[row_idx][col_idx]:
                start = (row_idx, col_idx)

    dist = calc_path_dist(track, start)
    cheats = get_cheats(track_positions, dist, 20, 100)

    # 1032135 is too high
    print(f'There are {len(cheats)} cheats available')

if __name__ == '__main__':
    part_1()
    part_2()