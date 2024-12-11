from common import get_input_lines
import re

def main():
    input = get_input_lines('day16.txt')
    right_sue = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    for line in input:
        sue_match = True
        for attribute in right_sue.keys():
            check = attribute + ': (\d+)'
            match = re.search(check, line)
            if match:
                if attribute in ['cats', 'trees']:
                    sue_match &= right_sue[attribute] < int(match.group(1))
                elif attribute in ['pomeranians', 'goldfish']:
                    sue_match &= right_sue[attribute] > int(match.group(1))
                else:
                    sue_match &= right_sue[attribute] == int(match.group(1))
        if sue_match:
            print(line)
            quit()

if __name__ == '__main__':
    main()