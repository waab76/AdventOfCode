from common import get_input_lines
import numpy as np

wires = {}

def evaluate(expression:str)->int:
    global wires
    if expression.isdigit():
        return np.uint16(expression)
    
    parts = wires[expression].split()
    
    val = 0
    if 1 == len(parts):
        val = np.uint16(evaluate(parts[0]))
    elif 'AND' in parts:
        val = np.uint16(evaluate(parts[0]) & evaluate(parts[2]))
    elif 'OR' in parts:
        val = np.uint16(evaluate(parts[0]) | evaluate(parts[2]))
    elif 'NOT' in parts:
        val = np.uint16(~ evaluate(parts[1]))
    elif 'LSHIFT' in parts:
        val = np.uint16(evaluate(parts[0]) << evaluate(parts[2]))
    elif 'RSHIFT' in parts:
        val = np.uint16(evaluate(parts[0]) >> evaluate(parts[2]))
    else:
        print('Dafuq...')
        quit()
    
    wires[expression] = str(val)
    return val

def main():
    global wires
    lines = get_input_lines('day_07.txt')
    for line in lines:
        parts = line.split(' -> ')
        wires[parts[1]] = parts[0]
    
    wires['b'] = '956'
    
    print(f'Value of a is {evaluate("a")}')

if __name__ == '__main__':
    main()