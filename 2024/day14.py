from common import get_input_lines, print_grid
import re
import numpy as np
from PIL import Image

def parse_robot(robot:str)->tuple:
    match = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', robot)
    start = (int(match.group(1)), int(match.group(2)))
    veloc = (int(match.group(3)), int(match.group(4)))
    return (start, veloc)

def find_final_pos(start:tuple, veloc:tuple, x_max:int, y_max:int, steps:int)->tuple:
    final_x = (start[0] + steps * veloc[0]) % x_max
    final_y = (start[1] + steps * veloc[1]) % y_max
    return (final_x, final_y)

def part_1():
    robots = get_input_lines('day14.txt')
    x_max = 101
    y_max = 103
    steps = 100
    quad_counts = [0,0,0,0]
    final_positions = list()

    for robot in robots:
        (start, veloc) = parse_robot(robot)
        final_pos = find_final_pos(start, veloc, x_max, y_max, steps)
        final_positions.append(final_pos)
        
    for pos in final_positions:
        if pos[0] < x_max //2 and pos[1] < y_max // 2:
            quad_counts[0] += 1
        elif pos[0] > x_max // 2 and pos[1] < y_max // 2:
            quad_counts[1] += 1
        elif pos[0] > x_max // 2 and pos[1] > y_max // 2:
            quad_counts[2] += 1
        elif pos[0] < x_max // 2 and pos[1] > y_max // 2:
            quad_counts[3] += 1
        else:
            pass # on the half-way lines
    
    safety_factor = quad_counts[0] * quad_counts[1] * quad_counts[2] * quad_counts[3]
    print(f'The safety factor is {safety_factor}')

def safety_score(positions:list, x_max:int, y_max:int)->int:
    quad_counts = [0,0,0,0]
    for pos in positions:
        if pos[0] < x_max //2 and pos[1] < y_max // 2:
            quad_counts[0] += 1
        elif pos[0] > x_max // 2 and pos[1] < y_max // 2:
            quad_counts[1] += 1
        elif pos[0] > x_max // 2 and pos[1] > y_max // 2:
            quad_counts[2] += 1
        elif pos[0] < x_max // 2 and pos[1] > y_max // 2:
            quad_counts[3] += 1
        else:
            pass # on the half-way lines
    return quad_counts[0] * quad_counts[1] * quad_counts[2] * quad_counts[3]
    
    safety_factor = quad_counts[0] * quad_counts[1] * quad_counts[2] * quad_counts[3]
def calc_and_print(robots:list, x_max:int, y_max:int, step:int, min_sf:int)->int:
    data = [['.' for col in range(x_max)] for row in range(y_max)]
    positions = list()
    for robot in robots:
        pos = find_final_pos(robot[0], robot[1], x_max, y_max, step)
        positions.append(pos)
        data[pos[1]][pos[0]] = '#'
    
    if safety_score(positions, x_max, y_max) < min_sf:
        print(f'Step {step}')
        print_grid(data)
        return safety_score(positions, x_max, y_max)
    return min_sf

def part_2():
    data = get_input_lines('day14.txt')
    x_max = 101
    y_max = 103
    max_steps = 10000
    robots = list()
    min_sf = 329069152
    min_sf_step = 0

    for robot in data:
        (start, veloc) = parse_robot(robot)
        robots.append((start, veloc))

    for step in range(1,max_steps):
        sf = calc_and_print(robots, x_max, y_max, step, min_sf)
        if sf < min_sf:
            min_sf = sf
            min_sf_step = step
    
    print(f'Min Safety Factor seen was {min_sf} on step {step}')


if __name__ == '__main__':
    part_1()
    part_2()