from common import get_input_lines
from itertools import permutations

def main():
    lines = get_input_lines('day13.txt')

    total_happiness = 0
    attendees = set()
    happies = dict()

    for line in lines:
        (first, _, gain_lose, happiness, _, _, _, _, _, _, second) = line.split()
        if 'lose' in gain_lose:
            happiness = -1 * int(happiness)
        else:
            happiness = int(happiness)
        happies.setdefault(first, dict())[second[:-1]] = happiness
        attendees.add(first)
        attendees.add(second[:-1])

    for arrangement in permutations(attendees):
        happiness = 0
        for idx in range(len(arrangement) - 1):
            happiness += happies[arrangement[idx]][arrangement[idx + 1]]
            happiness += happies[arrangement[idx + 1]][arrangement[idx]]
        happiness += happies[arrangement[0]][arrangement[len(arrangement) - 1]]
        happiness += happies[arrangement[len(arrangement) - 1]][arrangement[0]]
        if happiness > total_happiness:
            total_happiness = happiness

    print(f'Best total happiness is {total_happiness}')

if __name__ == '__main__':
    main()
