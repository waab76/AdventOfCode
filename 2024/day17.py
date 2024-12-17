from common import get_input_lines

OPCODE = ['adv', 'bxl', 'bst', 'jnz', 'bxc', 'out', 'bdv', 'cdv']

def combo(op:int, reg_a:int, reg_b:int, reg_c:int)->int:
    if op < 4:
        return op
    elif 4 == op:
        return reg_a
    elif 5 == op:
        return reg_b
    elif 6 == op:
        return reg_c
    else:
        print('Dafuq')
        quit()   

def parse_input():
    input = get_input_lines('day17.txt')
    reg_a = int(input[0].split()[2])
    reg_b = int(input[1].split()[2])
    reg_c = int(input[2].split()[2])
    program = list(map(int, input[4].split()[1].split(',')))

    return reg_a, reg_b, reg_c, program

def part_1():
    reg_a, reg_b, reg_c, program = parse_input()
    out = list()

    ptr = 0
    while ptr < len(program):
        op = program[ptr + 1]
        if OPCODE[program[ptr]] == 'adv':
            reg_a = reg_a // (2 ** combo(op, reg_a, reg_b, reg_c))
            ptr += 2
        elif OPCODE[program[ptr]] == 'bxl':
            reg_b ^= op
            ptr += 2
        elif OPCODE[program[ptr]] == 'bst':
            reg_b = combo(op, reg_a, reg_b, reg_c) % 8
            ptr += 2
        elif OPCODE[program[ptr]] == 'jnz':
            if 0 == reg_a:
                ptr += 2
            else:
                ptr = op
        elif OPCODE[program[ptr]] == 'bxc':
            reg_b ^= reg_c
            ptr += 2
        elif OPCODE[program[ptr]] == 'out':
            out.append(combo(op, reg_a, reg_b, reg_c) % 8)
            ptr += 2
        elif OPCODE[program[ptr]] == 'bdv':
            reg_b = reg_a // (2 ** combo(op, reg_a, reg_b, reg_c))
            ptr += 2
        elif OPCODE[program[ptr]] == 'cdv':
            reg_c = reg_a // (2 ** combo(op, reg_a, reg_b, reg_c))
            ptr += 2
        else:
              print('Dafuq?')
              quit()

    print(f'Progarm output: {out}')
    
def part_2():
    reg_a, reg_b, reg_c, program = parse_input()


if __name__ == '__main__':
    part_1()
    # part_2()