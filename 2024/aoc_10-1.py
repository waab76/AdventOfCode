from common import get_input_lines_as_grid, grid_get

def reachable_trailheads(map:list, row:int, col:int)->set:
    reachable = set()
    if 9 == int(map[row][col]):
        reachable.add((row,col))
    else:
        if int(grid_get(map, row, col - 1, '99')) == int(map[row][col]) + 1:
            reachable.update(reachable_trailheads(map, row, col - 1))
        if int(grid_get(map, row, col + 1, '99')) == int(map[row][col]) + 1:
            reachable.update(reachable_trailheads(map, row, col + 1))
        if int(grid_get(map, row - 1, col, '99')) == int(map[row][col]) + 1:
            reachable.update(reachable_trailheads(map, row - 1, col))
        if int(grid_get(map, row + 1, col, '99')) == int(map[row][col]) + 1:
            reachable.update(reachable_trailheads(map, row + 1, col))
    return reachable

def main():
    map = get_input_lines_as_grid('aoc_10.txt')

    sum = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if 0 == int(map[row][col]):
                sum += len(reachable_trailheads(map, row, col))

    print(f'The sum of reachable trailheads is {sum}')

if __name__ == '__main__':
    main()
