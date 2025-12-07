from common import get_input_lines, replace_char_at

def _part1(manifold:list[str]):
    splits = 0
    for row in range(len(manifold) - 1):
        for col in range(len(manifold[row])):
            if manifold[row][col] == 'S':
                if manifold[row+1][col] == '.':
                    manifold[row+1] = replace_char_at(manifold[row+1], col, '|')
            elif manifold[row][col] == '|':
                if manifold[row+1][col] == '.':
                    manifold[row+1] = replace_char_at(manifold[row+1], col, '|')
                elif manifold[row+1][col] == '^':
                    went_left = went_right = False
                    if col > 0 and manifold[row+1][col-1] in ['.', '|']:
                        manifold[row+1] = replace_char_at(manifold[row+1], col-1, '|')
                        went_left = True
                    if col < len(manifold[row]) and manifold[row+1][col+1] in ['.', '|']:
                        manifold[row+1] = replace_char_at(manifold[row+1], col+1, '|')
                        went_right = True
                    if went_left and went_right:
                        splits += 1
    print(f'Beam split {splits} times')

def _part2(manifold:list[str]):
    timelines = [[0 for _ in manifold[0]] for _ in manifold]
    for row in range(len(manifold) - 1):
        for col in range(len(manifold[row])):
            if manifold[row][col] == 'S':
                if manifold[row+1][col] == '|':
                    timelines[row+1][col] += 1
            elif manifold[row][col] == '|':
                if manifold[row+1][col] == '|':
                    timelines[row+1][col] += timelines[row][col]
                elif manifold[row+1][col] == '^':
                    if col > 0 and manifold[row+1][col-1] =='|':
                        timelines[row+1][col-1] += timelines[row][col]
                    if col < len(manifold[row]) and manifold[row+1][col+1] == '|':
                        timelines[row+1][col+1] += timelines[row][col]
    print(f'{sum(timelines[len(timelines) - 1])} timelines created')

def main():
    manifold = get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_07.txt')
    _part1(manifold)
    _part2(manifold)

if __name__ == '__main__':
    main()