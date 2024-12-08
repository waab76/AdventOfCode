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

similarity_score = 0

while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
        print(f'{left[0]} < {right[0]} - dropping left')
        left.pop(0)
    elif left[0] == right[0]:
        print(f'{left[0]} = {right[0]} - increasing similarty score by {left[0]}')
        similarity_score += left[0]
        right.pop(0)
    else:
        print(f'{left[0]} > {right[0]} - dropping right')
        right.pop(0)

print(f'The similarity score is {similarity_score}')
