from common import get_input_lines

def _parse_input(lines:list[str]) -> map:
    nodes = {}
    for line in lines:
        key = line[:line.index(':')]
        vals = line[line.index(':') + 1:].split()
        nodes[key] = vals
    return nodes

def _part1():
    pass

def _part2():
    pass

def main():
    data = get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_11.txt')
    nodes = _parse_input(data)

    _part1()
    _part2()

if __name__ == '__main__':
    main()