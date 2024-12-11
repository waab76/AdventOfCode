from numpy import vectorize
from functools import cache

@cache
def count_splits(stone:int, steps:int)->int:
    if steps == 0:
        return 1
    elif stone == 0:
        return count_splits(1, steps - 1)
    elif not len(str(stone)) % 2:
        stone_str = str(stone)
        first_half = int(stone_str[:len(stone_str)//2])
        back_half = int(stone_str[len(stone_str)//2:])
        return count_splits(first_half, steps - 1) + count_splits(back_half, steps - 1)
    else:
        return count_splits(stone * 2024, steps - 1)


def main():
    stones = vectorize(int)(list(open('aoc_11.txt')))
    blinks = 75

    total_stones = sum(count_splits(x, 75) for x in stones)
    
    print(f'After {blinks} blinks, there are {total_stones} stones')

if __name__ == '__main__':
    main()