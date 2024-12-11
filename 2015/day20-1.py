from functools import reduce

def get_factors(num:int)->set:
    return set(reduce(list.__add__, ([i, num//i] for i in range(1, int(num**.5) + 1) if num % i == 0)))

def presents_received(house_num:int)->int:
    factors = get_factors(house_num)
    factor_sum = sum(factors)
    print(f'Factors of {house_num} are {factors} which sum to {factor_sum}')
    return 10 * factor_sum

def main():
    target_presents = 34000000
    
    for house in range(500000, 3000000):
        received = presents_received(house)
        if received >= target_presents:
            print(f'House {house} gets {received} presents')
            break


if __name__ == '__main__':
    main()