from copy import copy
from functools import cache
from common import get_input_lines

nodes = {}

def _parse_input(lines:list[str]) -> map:
    for line in lines:
        key = line[:line.index(':')]
        vals = line[line.index(':') + 1:].split()
        nodes[key] = vals

@cache
def _count_paths(start: str, seen_fft: bool, seen_dac: bool) -> int:
    if start == 'out':
        if seen_fft and seen_dac:
            return 1
        return 0
    my_seen_fft = seen_fft or start == 'fft'
    my_seen_dac = seen_dac or start == 'dac'
    return sum(_count_paths(next, my_seen_fft, my_seen_dac) for next in nodes[start])

def _part1():
    paths = _count_paths('you', True, True)
    print(f'Paths to out: {paths}')
    
def _part2():
    paths = _count_paths('svr', False, False)
    print(f'Paths from svr to out that include fft and dac: {paths}')

def main():
    _parse_input(get_input_lines('aoc_11.txt'))

    _part1()
    _part2()

if __name__ == '__main__':
    main()