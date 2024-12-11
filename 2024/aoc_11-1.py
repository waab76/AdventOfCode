from numpy import vectorize

def blink(stones:list)->list:
    new_stones = list()
    for stone in stones:
        if 0 == stone:
            new_stones.append(1)
        elif not len(str(stone)) % 2:
            stone_str = str(stone)
            first_half = stone_str[:len(stone_str)//2]
            back_half = stone_str[len(stone_str)//2:]
            new_stones.append(int(first_half))
            new_stones.append(int(back_half))
        else:
            new_stones.append(stone * 2024)
    # print(f'{stones} becomes {new_stones}')
    return new_stones


def main():
    stones = vectorize(int)(list(open('aoc_11.txt')))
    blinks = 25

    for step in range(blinks):
        stones = blink(stones)
    
    print(f'After {blinks} blinks, there are {len(stones)} stones')

if __name__ == '__main__':
    main()
