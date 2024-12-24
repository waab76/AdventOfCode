from common import get_input_lines
from itertools import combinations

vals = {}
calcs = {}

def evaluate(key:str)->int:
    global vals, calcs

    if key in vals:
        return vals[key]

    a_key = calcs[key][0]
    op = calcs[key][1]
    b_key = calcs[key][2]
    a = vals[a_key] if a_key in vals else evaluate(a_key)
    b = vals[b_key] if b_key in vals else evaluate(b_key)

    if op == 'AND':
        vals[key] = a & b
    elif op == 'XOR':
        vals[key] = a ^ b
    elif op == 'OR':
        vals[key] = a | b

    return vals[key]


def part_1():
    global vals, calcs

    result = 0
    for key in sorted(calcs.keys(), reverse=True):
        if not key[0] == 'z':
            break
        result = result << 1
        result |= evaluate(key)

    print(f'The resulting number is {result}')


def part_2():
    global vals, calcs

    x, y, target_z = 0, 0, 0
    for key in sorted(vals.keys(), reverse=True):
        if 'y' in key:
            y = y << 1
            y |= vals[key]
        elif 'x' in key:
            x = x << 1
            x |= vals[key]
    target_z = x + y

    print(f'Attempting to satisfy {x} + {y} = {target_z}')            

if __name__ == '__main__':
    data = get_input_lines('day24.txt')

    for line in data:
        parts = line.split()
        if ':' in line:
            vals[parts[0][:-1]] = int(parts[1])
        elif '>' in line:
            calcs[parts[4]] = (parts[0], parts[1], parts[2])
            
    part_1()
    part_2()