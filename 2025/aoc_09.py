import itertools
from typing import List, Tuple
from common import get_input_lines

def _area(c1:Tuple[int,int], c2:Tuple[int,int])->int:
    return (abs(c2[0] - c1[0]) + 1) * (abs(c2[1] - c1[1]) + 1)

def _part1(corners:list[list[int]]):
    rectangles = itertools.combinations(corners, 2)
    max_area = 0
    for rect in rectangles:
        area = _area(rect[0], rect[1])
        if area > max_area:
            max_area = area
    print(f'Max area is {max_area}')

def _part2(corners:list[list[int]]):
    vert_lines: List[Tuple[int, Tuple[int, int]]] = []

    # For each line in the shape
    for i in range(len(corners)):
        p1 = corners[i - 1]
        p2 = corners[i]

        if p1[1] == p2[1]:
            vert_lines.append((p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])))

    # Sort the vertical events left to right and horiz by length descending
    vert_lines.sort(key=lambda x: x[0])
    
    print(f'Max area is {max_area}')



    # 51979885 is too low
    # 4738108384
    # 4489148850
    print(f'Max rectangle is {max_area}')

def main():
    corners = [[int(x) for x in line.split(',')] for line in get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_09.txt')]
    
    _part1(corners)
    _part2(corners)

if __name__ == '__main__':
    main()