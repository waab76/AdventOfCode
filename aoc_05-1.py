from common import get_input_lines
rules = []

def check_update(update:list) -> int:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return 0
    return int(update[len(update)//2])

def main():
    lines = get_input_lines('aoc_05.txt')
    global rules
    updates = []
    sum = 0

    for line in lines:
        if '|' in line:
            rules.append(line.split('|'))
        elif ',' in line:
            updates.append(line.split(','))

    for update in updates:
        sum += check_update(update)

    print(f'The sum from printable updates is {sum}')

if __name__ == '__main__':
    main()
