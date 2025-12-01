from common import get_input_lines

rotations = get_input_lines('aoc_01.txt')

dial_size = 100
current = 50
zeroes_seen = 0

for rotation in rotations:
    direction = -1 if 'L' in rotation[0] else 1
    distance = int(rotation[1:])
    next = (current + (direction * distance)) % 100
    print(f'Rotation {rotation} means move {direction * distance} from {current} to {next}')
    if next == 0:
        zeroes_seen += 1
    current = next

print(f'Zero seen {zeroes_seen} times')
