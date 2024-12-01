from common import get_input_lines

lines = get_input_lines('aoc_01.txt')

left = []
right = []

for line in lines:
    parts = line.split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

left.sort()
right.sort()

total_distance = 0

for i in range(len(left)):
    current_distance = abs(left[i] - right[i])
    print(f'The distance between {left[i]} and {right[i]} is {current_distance}')
    total_distance += current_distance

print(f'The total distance is {total_distance}')
