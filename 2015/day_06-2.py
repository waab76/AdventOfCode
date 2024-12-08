from common import get_input_lines

def parse_tuple(text:str)->tuple:
    parts = text.split(',')
    return (int(parts[0]), int(parts[1]))

def main():
    inputs = get_input_lines('day_06.txt')
    lights = [[0 for col in range(1000)] for row in range(1000)]

    for input in inputs:
        parts = input.split()
        command, start, end = '', tuple(), tuple()
        if len(parts) == 5:
            command, start, end = parts[1], parse_tuple(parts[2]), parse_tuple(parts[4])
        else:
            command, start, end = parts[0], parse_tuple(parts[1]), parse_tuple(parts[3])
        
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                if 'toggle' == command:
                    lights[row][col] += 2
                elif 'on' == command:
                    lights[row][col] += 1
                elif 'off' == command:
                    lights[row][col] -= 1
                    if lights[row][col] < 0:
                        lights[row][col] = 0
    
    total_brightness = 0
    for row in range(1000):
        for col in range(1000):
            total_brightness += lights[row][col]

    print(f'Total brightness of all lights is {total_brightness}')

if __name__ == '__main__':
    main()