from common import get_input_lines

def get_secret(curr:int, n:int=1)->int:
    for _ in range(n):
        next = (curr ^ (curr << 6)) & 0b111111111111111111111111
        next = (next ^ (next >> 5)) & 0b111111111111111111111111
        next = (next ^ (next << 11)) & 0b111111111111111111111111
        curr = next
    return curr

def part_1():
    secrets = get_input_lines('day22.txt')
    secrets = map(int, secrets)
    sum = 0
    for secret in secrets:
        sum += get_secret(secret, 2000)
    print(f'Sum of 2000th secrets is {sum}')

def part_2():
    secrets = get_input_lines('day22.txt')
    secrets = map(int, secrets)
    price_map = {}

    for secret in secrets:
        seen = set()
        last4 = (10, 10, 10, 10)
        for _ in range(2000):
            price = secret % 10
            secret = (secret ^ (secret << 6)) & 0b111111111111111111111111
            secret = (secret ^ (secret >> 5)) & 0b111111111111111111111111
            secret = (secret ^ (secret << 11)) & 0b111111111111111111111111
            new_price = secret % 10
            price_diff = new_price - price
            last4 = last4[1:] + (price_diff,)
            if last4 not in seen:
                seen.add(last4)
                price_map[last4] = price_map.get(last4, 0) + new_price
    print(max(price_map.values()))
            

if __name__ == '__main__':
    part_1()
    part_2()