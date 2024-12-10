from common import get_input_lines
import json

def sum_nums(data)->int:
    if isinstance(data, list):
        return sum(map(sum_nums, data))
    elif isinstance(data, dict):
        if 'red' in data.values():
            return 0
        return sum(map(sum_nums, data.values())) + sum(map(sum_nums, data.keys()))
    elif isinstance(data, str):
        return 0
    elif isinstance(data, int):
        return data


def main():
    data = json.loads(get_input_lines('day12.txt')[0])
    print(sum_nums(data))

if __name__ == '__main__':
    main()