from common import get_input_lines
import re

def main():
    lines = get_input_lines('aoc_03.txt')
    do = True
    total = 0
    for line in lines:
        matches = re.findall(r'do\(\)|don\'t\(\)|mul\(\d\d?\d?,\d\d?\d?\)', line)
        for match in matches:
            if 'don\'t' in match:
                do = False
            elif 'do' in match:
                do = True
            elif do:
                numbers = re.match(r'mul\((\d\d?\d?),(\d\d?\d?)\)', match)
                total += int(numbers[1]) * int(numbers[2])
    
    print(f'The total is: {total}')

if __name__ == '__main__':
    main()
