input = open('aoc_02.txt', 'r')
lines = input.readlines()

max_red = 12
max_green = 13
max_blue = 14

sum = 0

for line in lines:
    parts = line.strip().split(': ')
    game_number = int(parts[0][5:])
    rounds = parts[1].split('; ')
    possible = True
    for round in rounds:
        colors = round.split(', ')
        for color in colors:
            color_parts = color.split(' ')
            if 'red' == color_parts[1] and int(color_parts[0]) > max_red:
                possible = False
            elif 'blue' == color_parts[1] and int(color_parts[0]) > max_blue:
                possible = False
            elif 'green' == color_parts[1] and int(color_parts[0]) > max_green:
                possible = False
    if possible:
        print('Game {} is possible'.format(game_number))
        sum += game_number
print(sum)        