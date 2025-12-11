import math
from disjoint_union import DisjointUnion
from common import get_input_lines

def _calc_distance(junc1:list[int], junc2:list[int])->int:
    return sum((junc2[i] - junc1[i])**2 for i in range(3))

def _part1(junctions:list[list[int]]):
    du = DisjointUnion()
    distances = []
    for i in range(len(junctions)):
        du += i
        for j in range(i + 1, len(junctions)):
            distances.append((f'{i} {j}', _calc_distance(junctions[i], junctions[j])))
    distances.sort(key=lambda x: x[1])

    for _ in range(1000):
        candidates = [int(x) for x in distances.pop(0)[0].split()]
        du.union(candidates[0], candidates[1])
    
    du.sort(key=lambda x:len(x), reverse=True)
    product = math.prod(len(c) for c in du[:3])
    print(f'Product of top 3 {product}')    

def _part2(junctions):
    du = DisjointUnion()
    distances = []
    for i in range(len(junctions)):
        du += i
        for j in range(i + 1, len(junctions)):
            distances.append((f'{i} {j}', _calc_distance(junctions[i], junctions[j])))
    distances.sort(key=lambda x: x[1])

    candidates = []
    while len(du) > 1:
        candidates = [int(x) for x in distances.pop(0)[0].split()]
        du.union(candidates[0], candidates[1])
    
    product = math.prod(junctions[candidates[x]][0] for x in range(2))
    print(f'Product is {product}')    

def main():
    junctions = [[int(x) for x in line.split(',')] for line in get_input_lines('/Users/rcurtis/Workspace/AdventOfCode/2025/aoc_08.txt')]
    
    _part1(junctions)
    _part2(junctions)

if __name__ == '__main__':
    main()