from common import get_input_lines_as_grid

def calc_antinodes(tower_a:tuple, tower_b:tuple)->set:
    antinodes = set()
    row_diff = tower_a[0] - tower_b[0]
    col_diff = tower_a[1] - tower_b[1]

    test_loc = tower_a
    while test_loc[0] >= 0 and test_loc[0] < 50 and test_loc[1] >= 0 and test_loc[1] < 50:
        antinodes.add(test_loc)
        test_loc = (test_loc[0] + row_diff, test_loc[1] + col_diff)
    test_loc = tower_b
    while test_loc[0] >= 0 and test_loc[0] < 50 and test_loc[1] >= 0 and test_loc[1] < 50:
        antinodes.add(test_loc)
        test_loc = (test_loc[0] - row_diff, test_loc[1] - col_diff)
    
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

    # 1127 is too high
    print(f'Found {len(antinodes)} antinodes')

if __name__ == '__main__':
    main()