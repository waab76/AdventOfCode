import itertools
from common import get_input_lines, replace_char_at

def _parse_input(lines:list[str]) -> list[map]:
    machines = []

    for line in lines:
        lights = line[line.index('[') + 1:line.index(']')]
        buttons = [[int(a) for a in button.split(',')] for button in line[line.index(']') + 3:line.index('{') - 2].split(') (')]
        jolts = [int(j) for j in line[line.index('{') + 1:line.index('}')].split(',')]
        machines.append({'lights': lights, 'buttons': buttons, 'jolts': jolts})

    return machines

def _test_combo(target:str, buttons:list[list[int]]) -> bool:
    test = '.' * len(target)
    for button in buttons:
        for light in button:
            if test[light] == '.':
                test = replace_char_at(test, light, '#')
            else:
                test = replace_char_at(test, light, '.')
    return test == target

def _find_min_presses(machine:map) -> int:
    for presses in range(1, len(machine['buttons']) + 1):
        press_combos = itertools.combinations(machine['buttons'], presses)
        for combo in press_combos:
            if _test_combo(machine['lights'], combo):
                return presses
    return len(machine['buttons']) + 1

def _part1(machines:list[map]):
    presses = 0
    for machine in machines:
        presses += _find_min_presses(machine)
    print(f'Total minimum button mashes: {presses}')

def _part2():
    pass

def main():
    data = get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_10.txt')
    machines = _parse_input(data)
    
    _part1(machines)
    _part2()

if __name__ == '__main__':
    main()