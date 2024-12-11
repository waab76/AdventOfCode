from numpy import vectorize

def main():
    containers = vectorize(int)(list(open('day17.txt')))    
    valid_combos = 0

    for combo in range (1 << len(containers)):
        sum = 0
        for container in containers:
            if combo % 2 == 1:
                sum += container
            combo //= 2
        if sum == 150:
            valid_combos += 1

    print(f'Found {valid_combos} valid combinations')

if __name__ == '__main__':
    main()