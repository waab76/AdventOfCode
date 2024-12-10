import re

def iterate(input:str)->str:
    if 'z' == input[-1] and len(input) > 1:
        return iterate(input[:-1]) + 'a'
    elif 'z' == input[-1]:
        return 'a'
    else:
        return input[:-1] + chr(ord(input[-1]) + 1)

def is_valid(input:str)->bool:
    has_run = False
    for idx in range(len(input) - 2):
        if ord(input[idx + 1]) == ord(input[idx]) + 1 and ord(input[idx + 2]) == ord(input[idx + 1]) + 1:
            has_run = True
            break
    has_two_pair = bool(re.match(r'(.)\1.*(.)\2', input))
    no_bad_chars = bool(re.match(r'[^iol]{8}', input))

    return has_run and has_two_pair and no_bad_chars

def main():
    new_pass = iterate('hepxcrrq')
    while not is_valid(new_pass):
        new_pass = iterate(new_pass)
    
    # by reasoning -> hepxxyzz -> heqaabcc
    print(new_pass)

    

if __name__ == '__main__':
    main()