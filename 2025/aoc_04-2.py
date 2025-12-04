from common import get_input_lines_as_grid, grid_get

def _is_accessible(grid:list, row:int, col:int) -> bool:
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighboring_rolls = 0

    for neighbor in neighbors:
        if not grid_get(grid, row + neighbor[0], col + neighbor[1], '.') == '.':
            neighboring_rolls += 1

    return neighboring_rolls < 4

def _do_removals(grid:list) -> int:
    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@' and _is_accessible(grid, row, col):
                grid[row][col] = '.'
                accessible_rolls += 1
    return accessible_rolls

def main():
    grid = get_input_lines_as_grid('aoc_04.txt')
    removed_rolls = 0

    just_removed = _do_removals(grid)
    while just_removed > 0:
        removed_rolls += just_removed
        just_removed = _do_removals(grid)

    print(f'Removed rolls: {removed_rolls}')

if __name__ == '__main__':
    main()