from common import get_input_lines_as_grid

def calc_antinodes(tower_a:tuple, tower_b:tuple)->set:
    antinodes = set()
    row_diff = tower_a[0] - tower_b[0]
    col_diff = tower_a[1] - tower_b[1]

    ext_1 = (tower_a[0] + row_diff, tower_a[1] + col_diff)
    if ext_1[0] >= 0 and ext_1[0] < 50 and ext_1[1] >= 0 and ext_1[1] < 50:
        antinodes.add(ext_1)
    ext_2 = (tower_b[0] - row_diff, tower_b[1] - col_diff)
    if ext_2[0] >= 0 and ext_2[0] < 50 and ext_2[1] >= 0 and ext_2[1] < 50:
        antinodes.add(ext_2)

    if 0 == row_diff % 3 and 0 == col_diff % 3:
        print(f'We should have internal antinodes')
        # Thanks for not including this case in the input
    
    return antinodes

def calc_all_antinodes(tower_locs:list)->set:
    antinodes = set()
    while len(tower_locs) > 1:
        tower_a = tower_locs.pop()
        for tower_b in tower_locs:
            antinodes.update(calc_antinodes(tower_a, tower_b))
    return antinodes

def main():
    tower_map = get_input_lines_as_grid('aoc_08.txt')
    tower_locs = dict()
    antinodes = set()

    for row in range(len(tower_map)):
        for col in range(len(tower_map[0])):
            if '.' == tower_map[row][col]:
                continue
            else:
                if tower_map[row][col] not in tower_locs:
                    tower_locs[tower_map[row][col]] = list()
                tower_locs[tower_map[row][col]].append((row, col))
    
    for freq in tower_locs.keys():
        antinodes.update(calc_all_antinodes(tower_locs[freq]))

    print(f'Found {len(antinodes)} antinodes')

if __name__ == '__main__':
    main()