from common import get_input_lines

def main():
    input = get_input_lines('day01.txt')[0]
    on_floor = 0
    for command in input:
        if '(' == command:
            on_floor += 1
        elif ')' == command:
            on_floor -= 1

    print(f'Santa finishes on floor {on_floor}')

if __name__ == '__main__':
    main()
