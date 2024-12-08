from common import get_input_lines

def main():
    lines = get_input_lines('day08.txt')
    total = 0

    for line in lines:
        char_diff = 2
        for char in line:
            if '\\' == char or '"' == char:
                char_diff += 1
        total += char_diff
    print(total)

if __name__ == '__main__':
    main()