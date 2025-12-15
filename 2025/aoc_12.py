from copy import copy
from functools import cache
from common import get_input_lines

nodes = {}

def _parse_input(lines:list[str]) -> map:
    gifts = [lines[1:4], lines[6:9], lines[11:14], lines[16:19], lines[21:24], lines[26:29]]
    trees = [{'x': int(line.split(':')[0].split('x')[0]), 
                'y': int(line.split(':')[0].split('x')[1]),
                'counts': [int(count) for count in line.split(':')[1].split()]} for line in lines[30:]]
    return gifts, trees

def main():
    gifts, trees = _parse_input(get_input_lines('2025/aoc_12.txt'))
    gift_sizes = [sum(row.count('#') for row in gift) for gift in gifts]

    guaranteed_fits = 0
    guaranteed_no_fits = 0

    for tree in trees:
        gift_count = sum(tree['counts'])
        max_gifts = (tree['x'] // 3) * (tree['y'] // 3)
        if gift_count <= max_gifts:
            guaranteed_fits += 1
        
        total_area = tree['x'] * tree['y']
        gift_area = sum(tree['counts'][i] * gift_sizes[i] for i in range(len(gifts)))
        if total_area < gift_area:
            guaranteed_no_fits += 1
    
    print(f'Of {len(trees)} trees, {guaranteed_no_fits} cannot work and {guaranteed_fits} absolutely will')


    print(f'Done')


if __name__ == '__main__':
    main()