from common import get_input_lines

def main():
    lines = get_input_lines('aoc_04.txt')
    count = 0

    rows = len(lines)
    cols = len(lines[0])

    for row in range(rows):
        for col in range(cols):
            if 'X' == lines[row][col]:
                # Check N
                if row - 3 >= 0:
                    count += 1 if 'M' == lines[row - 1][col] and 'A' == lines[row - 2][col] and 'S' == lines[row - 3][col] else 0
                # Check NE
                if row - 3 >= 0 and col + 3 < cols:
                    count += 1 if 'M' == lines[row - 1][col + 1] and 'A' == lines[row - 2][col + 2] and 'S' == lines[row - 3][col + 3] else 0
                # Check E
                if col + 3 < cols:
                    count += 1 if 'M' == lines[row][col + 1] and 'A' == lines[row][col + 2] and 'S' == lines[row][col + 3] else 0
                # Check SE
                if row + 3 < rows and col + 3 < cols:
                    count += 1 if 'M' == lines[row + 1][col + 1] and 'A' == lines[row + 2][col + 2] and 'S' == lines[row + 3][col + 3] else 0
                # Check S
                if row + 3 < rows:
                    count += 1 if 'M' == lines[row + 1][col] and 'A' == lines[row + 2][col] and 'S' == lines[row + 3][col] else 0
                # Check SW
                if row + 3 < rows and col - 3 >= 0:
                    count += 1 if 'M' == lines[row + 1][col - 1] and 'A' == lines[row + 2][col - 2] and 'S' == lines[row + 3][col - 3] else 0
                # Check W
                if col - 3 >= 0:
                    count += 1 if 'M' == lines[row][col - 1] and 'A' == lines[row][col - 2] and 'S' == lines[row][col - 3] else 0
                # Check NW
                if row - 3 >= 0 and col - 3 >= 0:
                    count += 1 if 'M' == lines[row - 1][col - 1] and 'A' == lines[row - 2][col - 2] and 'S' == lines[row - 3][col - 3] else 0
    print(f'Found {count} instances of XMAS')

if __name__ == '__main__':
    main()
