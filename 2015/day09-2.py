from common import get_input_lines
from itertools import permutations

def main():
    input = get_input_lines('day09.txt')
    stops = set()
    distances = dict()

    for line in input:
        parts = line.split()
        stops.add(parts[0])
        stops.add(parts[2])
        distances.setdefault(parts[0], dict())[parts[2]] = int(parts[4])
        distances.setdefault(parts[2], dict())[parts[0]] = int(parts[4])
    
    longest = 0

    for items in permutations(stops):
        dist = 0
        for idx in range(len(items) - 1):
            dist += distances[items[idx]][items[idx+1]]
        if dist > longest:
            longest = dist

    print(longest)

if __name__ == '__main__':
    main()