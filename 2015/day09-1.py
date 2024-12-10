from common import get_input_lines
from functools import cmp_to_key

def compare(left:tuple, right:tuple)->int:
    return left[2] - right[2]

def main():
    input = get_input_lines('day09.txt')
    stops = set()
    visited = set()
    paths = list()

    for line in input:
        parts = line.split()
        path = (parts[0], parts[2], int(parts[4]))
        stops.add(path[0])
        stops.add(path[1])
        paths.append(path)

    paths = sorted(paths, key=cmp_to_key(lambda left, right: left[2] - right[2]))
    first_leg = paths.pop(0)
    visited.add(first_leg[0])
    visited.add(first_leg[1])
    point_a, point_b = first_leg[0], first_leg[1]
    total_distance = first_leg[2]
    print(f'Visited {visited} from {point_a} to {point_b} with distance {total_distance}')
    
    while len(visited) < len(stops):
        candidates = list(filter(lambda path: point_a in path or point_b in path, paths))
        shortest = sorted(candidates, key=cmp_to_key(lambda left, right: left[2] - right[2]))[0]
        print(f'Shortest candidate path: {shortest}')
        if shortest[0] in visited and shortest[1] in visited:
            paths.remove(shortest)
            print(f'Already been to these cities')
            continue

        if point_a in shortest:
            point_a = shortest[0] if point_a == shortest[1] else shortest[1]
            visited.add(point_a)
        else:
            point_b = shortest[0] if point_b == shortest[1] else shortest[1]
            visited.add(point_b)
        total_distance += shortest[2]
        paths.remove(shortest)
        print(f'Visited {visited} from {point_a} to {point_b} with distance {total_distance}')

        

if __name__ == '__main__':
    main()