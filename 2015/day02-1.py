from common import get_input_lines

def paper_required(dims:list)->int:
    l, w, h = dims[0], dims[1], dims[2]

    sides = [2 * l * w, 2 * l * h, 2 * w * h]
    sides.sort()

    return sides[0]//2 + sides[0] + sides[1] + sides[2]

def main():
    presents = get_input_lines('day02.txt')
    total_paper = 0

    for present in presents:
        dims = [int(x) for x in present.split('x')]
        total_paper += paper_required(dims)

    print(f'The elves need {total_paper} sq ft of paper')

if __name__ == '__main__':
    main()
