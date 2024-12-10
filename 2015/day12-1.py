from common import get_input_lines
import re

def space(data):
    return ' '

def main():
    data = get_input_lines('day12.txt')[0]
    tokens = re.sub(r'[",:\[\]\{\}]', space, data).split()
    print(tokens)

    sum = 0
    for token in tokens:
        if token.isdigit() or re.match(r'-[0-9]+', token):
            sum += int(token)
    print(sum)

if __name__ == '__main__':
    main()