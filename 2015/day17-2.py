from numpy import vectorize
import json

def main():
    containers = vectorize(int)(list(open('day17.txt')))    
    valid_combo_sizes = dict()

    for combo in range (1 << len(containers)):
        sum = 0
        size = 0
        for container in containers:
            if combo % 2 == 1:
                sum += container
                size += 1
            combo //= 2
        if sum == 150:
            if size not in valid_combo_sizes:
                valid_combo_sizes[size] = 1
            else:
                valid_combo_sizes[size] += 1

    print(json.dumps(valid_combo_sizes, indent=2))

if __name__ == '__main__':
    main()