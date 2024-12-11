from common import get_input_lines
import re

def main():
    lines = get_input_lines('day19.txt')
    
    replacements = dict()
    molecule = lines[-1]
    uniques = set()

    for line in lines:
        if 0 == len(line):
            break
        parts = line.split(' => ')
        if parts[0] not in replacements:
            replacements[parts[0]] = list()
        replacements[parts[0]].append(parts[1])

    for to_rep in replacements.keys():
        matches = re.finditer(to_rep, molecule)
        for match in matches:
            for rep in replacements[to_rep]:
                candidate = molecule[:match.start()] + rep + molecule[match.end():]
                uniques.add(candidate)
    
    print(f'Can generate {len(uniques)} unique molecules in 1 step')

if __name__ == '__main__':
    main()