from common import get_input_lines

DIR = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

def main():
    moves = get_input_lines('day03.txt')[0]
    santa_pos, robo_pos = (0,0), (0,0)
    visited = set()
    visited.add(santa_pos)

    for i in range(len(moves)):
        if not i % 2:
            santa_pos = (santa_pos[0] + DIR[moves[i]][0], santa_pos[1] + DIR[moves[i]][1])
            visited.add(santa_pos)
        else:
            robo_pos = (robo_pos[0] + DIR[moves[i]][0], robo_pos[1] + DIR[moves[i]][1])
            visited.add(robo_pos)

    print(f'Santa and Robo Santa visited {len(visited)} houses')

if __name__ == '__main__':
    main()