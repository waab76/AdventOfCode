from common import get_input_lines

def main():
    lines = get_input_lines('day08.txt')
    total = 0

    for line in lines:
        diff_chars = 0
        i = 0
        while i < len(line):
            if '"' == line[i]:
                diff_chars += 1
            elif '\\' == line[i]:
                diff_chars += 1
                if 'x' == line[i + 1]:
                    diff_chars += 2
                    i += 2
                i += 1
            i += 1
        total += diff_chars
    print(total)

if __name__ == '__main__':
    main()