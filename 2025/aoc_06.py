from math import prod
from common import get_input_lines

def _part1(numbers:list[list[int]], operations:list[str]):
    answer_sum = 0
    for problem in range(len(operations)):
        problem_answer = 1 if operations[problem] == '*' else 0
        for value in range(len(numbers)):
            if operations[problem] == '*':
                problem_answer *= numbers[value][problem]
            else:
                problem_answer += numbers[value][problem]
        answer_sum += problem_answer
    print(f'Sum of answers is {answer_sum}')

def _part2():
    lines = get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_06.txt')
    answer_sum = 0
    
    nxt_prob_idx = 0
    try:
        while True:
            curr_prob_idx = nxt_prob_idx
            nxt_prob_idx += 1
            while lines[len(lines)-1][nxt_prob_idx] == ' ':
                nxt_prob_idx += 1
            problem = ''
            for col in range(curr_prob_idx, nxt_prob_idx - 1):
                for row in range(len(lines) - 1):
                    problem += lines[row][col]
                problem += lines[len(lines)-1][curr_prob_idx]
            problem = problem[:-1]
            problem_ans = eval(problem)
            print(f'{problem}={problem_ans}')
            answer_sum += problem_ans
    except:
        problem = ''
        for col in range(curr_prob_idx, len(lines[0])):
            for row in range(len(lines) - 1):
                problem += lines[row][col]
            problem += lines[len(lines)-1][curr_prob_idx]
        problem = problem[:-1]
        problem_ans = eval(problem)
        print(f'{problem}={problem_ans}')
        answer_sum += problem_ans

    # 25168294931249 is too high, 9029755694362 is too low, 9029931401920
    print(f'Sum of answers is {answer_sum}')

def main():
    lines = get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_06.txt')
    operations = lines.pop().split()
    numbers = [[int(number) for number in line.split()] for line in lines]
    _part1(numbers, operations)
    _part2()

if __name__ == '__main__':
    main()