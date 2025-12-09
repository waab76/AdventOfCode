from common import get_input_lines

def _parse_input():
    input = get_input_lines('/Volumes/CaseSensitive/Workspace/AdventOfCode/2025/aoc_05.txt')
    divide = input.index('')
    ranges = [[int(a) for a in range.split('-')] for range in input[:divide]]
    ingredients = input[divide + 1:]

    return ranges, ingredients

def _is_fresh(ranges:list[list[int]], ingredient:int)->bool:
    for range in ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            return True
    return False

def _part1():
    ranges, ingredients = _parse_input()
    fresh_ingredients = 0

    for ingredient in ingredients:
        if _is_fresh(ranges, int(ingredient)):
            fresh_ingredients += 1

    print(f'Part 1 - Fresh ingredient count: {fresh_ingredients}')
    
def _part2():
    ranges, _ = _parse_input()

    total_fresh_ingredients = 0

    ranges.sort(key=lambda x: x[0])
    first_range = ranges.pop(0)
    range_start, range_end = first_range[0], first_range[1]

    while len(ranges) > 0:
        if ranges[0][0] <= range_end:
            overlapping_range = ranges.pop(0)
            if overlapping_range[1] > range_end:
                range_end = overlapping_range[1]
        else:
            total_fresh_ingredients += (range_end - range_start) + 1
            next_range = ranges.pop(0)
            range_start, range_end = next_range[0], next_range[1]

    total_fresh_ingredients += (range_end - range_start) + 1

    print(f'Part 2 - Total fresh ingredients {total_fresh_ingredients}')

def main():
    _part1()
    _part2() # 4803286144483 is too low

if __name__ == '__main__':
    main()