from common import get_input_lines

def see_say(input:str)->str:
    output = ''
    ptr = 0
    while ptr < len(input):
        digit = input[ptr]
        count = 1
        while ptr + 1 < len(input) and input[ptr] == input[ptr + 1]:
            count += 1
            ptr += 1
        output += str(count)
        output += digit
        ptr += 1
    # print(f'{input} -> {output}')
    return output

def main():
    start = '1113122113'

    for iterations in range(50):
        start = see_say(start)
    
    print(len(start))

if __name__ == '__main__':
    main()