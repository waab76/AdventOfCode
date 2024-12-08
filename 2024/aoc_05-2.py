from common import get_input_lines
rules = []

def correctly_ordered(update:list) -> bool:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def fix_update(update:list) -> int:
    while not correctly_ordered(update):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    update[update.index(rule[0])], update[update.index(rule[1])] = rule[1],rule[0]
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
        if not correctly_ordered(update):
            sum += fix_update(update)

    print(f'The sum from corrected updates is {sum}')

if __name__ == '__main__':
    main()
