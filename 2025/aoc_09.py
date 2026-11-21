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

def _edges(corners:list[list[int]]) -> Tuple[list, list]:
    # Vertical edges as (x, y_lo, y_hi), horizontal edges as (y, x_lo, x_hi)
    vert, horiz = [], []
    for i in range(len(corners)):
        (x1, y1), (x2, y2) = corners[i - 1], corners[i]
        if x1 == x2:
            vert.append((x1, min(y1, y2), max(y1, y2)))
        else:
            horiz.append((y1, min(x1, x2), max(x1, x2)))
    return vert, horiz

def _edge_cuts_interior(vert:list, horiz:list, xmin:int, xmax:int, ymin:int, ymax:int) -> bool:
    # True if any loop edge passes through the open interior of the rectangle
    for x, lo, hi in vert:
        if xmin < x < xmax and lo < ymax and hi > ymin:
            return True
    for y, lo, hi in horiz:
        if ymin < y < ymax and lo < xmax and hi > xmin:
            return True
    return False

def _inside(vert:list, px:float, py:float) -> bool:
    # Ray cast to the right. px/py are half-integers so they never sit on an edge.
    crossings = sum(1 for x, lo, hi in vert if x > px and lo < py < hi)
    return crossings % 2 == 1

def _part2(corners:list[list[int]]):
    vert, horiz = _edges(corners)

    # Check candidates largest first; the first valid one is the answer
    rectangles = sorted(itertools.combinations(corners, 2), key=lambda r: _area(r[0], r[1]), reverse=True)
    for c1, c2 in rectangles:
        xmin, xmax = sorted((c1[0], c2[0]))
        ymin, ymax = sorted((c1[1], c2[1]))
        if _edge_cuts_interior(vert, horiz, xmin, xmax, ymin, ymax):
            continue
        # No edge cuts in, so the whole interior is either inside or outside the loop
        if _inside(vert, xmin + 0.5, ymin + 0.5):
            print(f'Max rectangle is {_area(c1, c2)}')
            return
    print('No valid rectangle found')

    # Earlier attempts: 51979885 is too low, 4489148850

def main():
    corners = [[int(x) for x in line.split(',')] for line in get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_09.txt')]
    
    _part1(corners)
    _part2(corners)

if __name__ == '__main__':
    main()