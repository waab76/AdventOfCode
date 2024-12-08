from common import get_input_lines
import re

def is_nice(test:str)->bool:
    pairs_test = False
    for i in range(len(test)):
        if test[i:i+2] in test[i+2:]:
            pairs_test = True
            break
    repeat_test = False
    for i in range(2, len(test)):
        if test[i] == test[i - 2]:
            repeat_test = True
            break
    return pairs_test and repeat_test

def main():
    strings = get_input_lines('day05.txt')
    nice = 0
    for string in strings:
        if is_nice(string):
            nice += 1

    print(f'Found {nice} nice strings')

if __name__ == '__main__':
    main()