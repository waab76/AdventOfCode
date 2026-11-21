import itertools
from functools import cache
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

def _press_patterns(buttons:list[list[int]], counters:int) -> dict:
    # Every way to press each button 0 or 1 times (the part 1 search space),
    # grouped by the odd/even pattern it leaves on the counters.
    # Value: list of (number of presses, how much each counter goes up)
    patterns = {}
    for presses in range(len(buttons) + 1):
        for combo in itertools.combinations(buttons, presses):
            added = [0] * counters
            for button in combo:
                for counter in button:
                    added[counter] += 1
            parity = tuple(a % 2 for a in added)
            patterns.setdefault(parity, []).append((presses, added))
    return patterns

def _min_joltage_presses(machine:map) -> int:
    patterns = _press_patterns(machine['buttons'], len(machine['jolts']))

    @cache
    def solve(targets:tuple) -> float:
        if not any(targets):
            return 0
        best = float('inf')
        parity = tuple(t % 2 for t in targets)
        # Buttons pressed an odd number of times must fix the parity (like part 1).
        # Press those once, then everything left is even: halve it and double the cost.
        for presses, added in patterns.get(parity, []):
            if all(a <= t for a, t in zip(added, targets)):
                rest = tuple((t - a) // 2 for a, t in zip(added, targets))
                best = min(best, presses + 2 * solve(rest))
        return best

    return solve(tuple(machine['jolts']))

def _part2(machines:list[map]):
    presses = sum(_min_joltage_presses(machine) for machine in machines)
    print(f'Total minimum joltage presses: {presses}')

def main():
    data = get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_10.txt')
    machines = _parse_input(data)

    _part1(machines)
    _part2(machines)

if __name__ == '__main__':
    main()