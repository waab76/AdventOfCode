import itertools
from common import get_input_lines

def _breaks(p1, p2, c1, c2):
    # If the line is vertical (same X on both points)
    if p1[0] == p2[0]:
        # If the X is between the two corners
        if min(c1[0], c2[0]) < p1[0] < max(c1[0], c2[0]):
            # Break if upper and lower point bracket the upper or lower corner or are both inside the box
            return min(p1[1], p2[1]) < c1[1] < max(p1[1], p2[1]) \
                or min(p1[1], p2[1]) < c2[1] < max(p1[1], p2[1]) \
                or min(c1[1], c2[1]) < min(p1[1], p2[1]) < max(p1[1], p2[1]) < max(c1[1], c2[1])
    elif p1[1] == p2[1]:
        if min(c1[1], c2[1]) < p1[1] < max(c1[1], c2[1]):
            return min(p1[0], p2[0]) < c1[0] < max(p1[0], p2[0]) \
                or min(p1[0], p2[0]) < c2[0] < max(p1[0], p2[0]) \
                or min(c1[0], c2[0]) < min(p1[0], p2[0]) < max(p1[0], p2[0]) < max(c1[0], c2[0])
    return False

def _part1(corners:list[list[int]]):
    rectangles = itertools.combinations(corners, 2)
    max_area = 0
    for rect in rectangles:
        area = (abs(rect[1][0] - rect[0][0]) + 1) * (abs(rect[1][1] - rect[0][1]) + 1)
        if area > max_area:
            max_area = area
    print(f'Max area is {max_area}')

def _part2(corners:list[list[int]]):
    # Get all rectangles
    rectangles = itertools.combinations(corners, 2)
    by_size = []
    # Calculate and store sizes as key with corners as value
    for rect in rectangles:
        area = (abs(rect[1][0] - rect[0][0]) + 1) * (abs(rect[1][1] - rect[0][1]) + 1)
        by_size.append((area, rect))
    # Order by size, desc
    by_size.sort(key=lambda x: x[0], reverse=True)
    # For each rectangle
    for candidate in by_size:
        is_intact = True
        # For each line in the big shape
        for i in range(len(corners)):
            p1 = corners[i - 1]
            p2 = corners[i]
            # If line crosses one of rectangle lines, it doesn't win
            if _breaks(p1, p2, candidate[1][0], candidate[1][1]):
                is_intact = False
                break
        # No lines cross = winner
        if is_intact:
            # 1513792010 is too high
            print(f'Winner is size {candidate[0]}')
            return

def main():
    corners = [[int(x) for x in line.split(',')] for line in get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_09.txt')]
    
    _part1(corners)
    _part2(corners)

if __name__ == '__main__':
    main()