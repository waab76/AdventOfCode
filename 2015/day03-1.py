from common import get_input_lines

DIR = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

def main():
    moves = get_input_lines('day03.txt')[0]
    santa_pos = (0,0)
    visited = set(santa_pos)

    for move in moves:
        santa_pos = (santa_pos[0] + DIR[move][0], santa_pos[1] + DIR[move][1])
        visited.add(santa_pos)

    print(f'Santa visited {len(visited)} houses')

if __name__ == '__main__':
    main()
