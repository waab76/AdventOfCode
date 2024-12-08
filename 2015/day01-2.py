from common import get_input_lines

def main():
    input = get_input_lines('day01.txt')[0]
    on_floor = 0
    instruction = 0

    for command in input:
        instruction += 1
        if '(' == command:
            on_floor += 1
        elif ')' == command:
            on_floor -= 1
        
        if on_floor < 0:
            break

    print(f'Santa entered the basement on instruction {instruction}')

if __name__ == '__main__':
    main()
