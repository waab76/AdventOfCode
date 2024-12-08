from common import get_input_lines

def ribbon_required(dims:list)->int:
    l, w, h = dims[0], dims[1], dims[2]

    sides = [2 * (l + w), 2 * (l + h), 2 * (w + h)]
    sides.sort()

    return sides[0] + (l * w * h)

def main():
    presents = get_input_lines('day02.txt')
    total_ribbon = 0

    for present in presents:
        dims = [int(x) for x in present.split('x')]
        total_ribbon += ribbon_required(dims)

    print(f'The elves need {total_ribbon} ft of ribbon')

if __name__ == '__main__':
    main()
