from common import get_input_lines
lines = []

def nw_se_mas(row:int, col:int) -> bool:
    return ('M' == lines[row - 1][col - 1] and 'S' == lines[row + 1][col + 1]) \
        or ('S' == lines[row - 1][col - 1] and 'M' == lines[row + 1][col + 1])

def sw_ne_mas(row:int, col:int) -> bool:
    return ('M' == lines[row + 1][col - 1] and 'S' == lines[row - 1][col + 1]) \
        or ('S' == lines[row + 1][col - 1] and 'M' == lines[row - 1][col + 1])

def main():
    global lines
    lines = get_input_lines('aoc_04.txt')
    count = 0

    rows = len(lines)
    cols = len(lines[0])

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if 'A' == lines[row][col]:
                count += 1 if nw_se_mas(row,col) and sw_ne_mas(row,col) else 0

    print(f'Found {count} instances of X-MAS')

if __name__ == '__main__':
    main()