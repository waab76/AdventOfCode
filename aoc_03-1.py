from common import get_input_lines
import re

def main():
    lines = get_input_lines('aoc_03.txt')
    total = 0
    for line in lines:
        matches = re.findall(r'mul\((\d\d?\d?),(\d\d?\d?)\)', line)
        for match in matches:
            total += int(match[0]) * int(match[1])
    
    print(f'The total is: {total}')

if __name__ == '__main__':
    main()
