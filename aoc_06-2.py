from common import get_input_lines, grid_get
import copy

UP, DOWN, RIGHT, LEFT = (-1, 0), (1, 0), (0, 1), (0, -1)

def check_for_loop(loop_map:list, row:int, col:int)->bool:
    curr_pos = (61, 78, UP)
    visited = set()

    if not '.' == loop_map[row][col]:
        return False
    
    loop_map[row][col] = '#'

    while curr_pos[0] >= 0 and curr_pos[0] < len(loop_map) \
          and curr_pos[1] >= 0 and curr_pos[1] < len(loop_map[0]):
        
        visited.add(curr_pos)
        next_pos = (curr_pos[0] + curr_pos[2][0], curr_pos[1] + curr_pos[2][1], curr_pos[2])

        if '#' == grid_get(grid=loop_map, row=next_pos[0], col=next_pos[1]):
            if UP == curr_pos[2]:
                next_pos = (curr_pos[0], curr_pos[1], RIGHT)
            elif RIGHT == curr_pos[2]:
                next_pos = (curr_pos[0], curr_pos[1], DOWN)
            elif DOWN == curr_pos[2]:
                next_pos = (curr_pos[0], curr_pos[1], LEFT)
            else:
                next_pos = (curr_pos[0], curr_pos[1], UP)

        if next_pos in visited:
            return True
        
        curr_pos = next_pos

    return False


def main():
    room_map = get_input_lines('aoc_06.txt')
    loops = 0

    for row in range(len(room_map)):
        for col in range(len(room_map[0])):
            if check_for_loop(copy.deepcopy(room_map), row, col):
                loops += 1

    print(f'Found {loops} loops')

if __name__ == '__main__':
    main()