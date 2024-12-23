from common import get_input_lines
from itertools import combinations
import networkx

def adjacency_list(links:list)->dict:
    network = dict()
    for link in links:
        ends = link.split('-')
        network.setdefault(ends[0], list()).append(ends[1])
        network.setdefault(ends[1], list()).append(ends[0])
    return network

def part_1():
    links = get_input_lines('day23.txt')
    network = adjacency_list(links)

    subnets = set()
    for key in network.keys():
        if key[0] == 't':
            for check in combinations(network[key], 2):
                if check[1] in network[check[0]]:
                    subnet = [key, check[0], check[1]]
                    subnet.sort()
                    subnets.add('-'.join(subnet))
    print(f'Found {len(subnets)} networks of size 3 with a computer that starts with t')

def part_2():
    links = get_input_lines('day23.txt')
    graph = networkx.Graph()
    graph.add_edges_from(link.split('-') for link in links)

    max_clique = None
    max_size = 0

    for clique in networkx.find_cliques(graph):
        if len(clique) > max_size:
            max_clique = clique
            max_size = len(clique)
    
    print(f'The password is {",".join(sorted(max_clique))}')
            

if __name__ == '__main__':
    part_1()
    part_2()