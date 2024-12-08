from common import get_input_lines
import re

def is_nice(test:str)->bool:
    strings_test = 'ab' not in test and \
                   'cd' not in test and \
                   'pq' not in test and \
                   'xy' not in test
    vowels_test = len(re.findall(r'[aeiou]', test)) > 2
    repeat_test = False
    for i in range(1, len(test)):
        if test[i] == test[i - 1]:
            repeat_test = True
            break
    return strings_test and vowels_test and repeat_test

def main():
    strings = get_input_lines('day05.txt')
    nice = 0
    for string in strings:
        if is_nice(string):
            nice += 1

    print(f'Found {nice} nice strings')

if __name__ == '__main__':
    main()