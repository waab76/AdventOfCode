from common import get_input_lines, grid_get

UP, DOWN, RIGHT, LEFT = (-1, 0), (1, 0), (0, 1), (0, -1)

def main():
    map = get_input_lines('aoc_06.txt')

    curr_pos = tuple()
    facing = tuple()
    visited = set()

    # Find guard position and facing
    for row in range(len(map)):
        if '^' in map[row]:
            curr_pos = (row, map[row].index('^'))
            facing = UP
            break

    # While guard is in mapped area
    while curr_pos[0] >= 0 and curr_pos[0] < len(map) \
          and curr_pos[1] >= 0 and curr_pos[1] < len(map[0]):
        # Mark current position visited
        visited.add(curr_pos)

        # Caclulate next position
        next_pos = (curr_pos[0] + facing[0], curr_pos[1] + facing[1])

        # If obstructed, turn right, continue
        if '#' == grid_get(grid=map, row=next_pos[0], col=next_pos[1]):
            if UP == facing:
                facing = RIGHT
            elif RIGHT == facing:
                facing = DOWN
            elif DOWN == facing:
                facing = LEFT
            else:
                facing = UP
            continue

        # Take a step
        curr_pos = next_pos

    # Count visited positions
    print(f'Visited {len(visited)} positions')

if __name__ == '__main__':
    main()