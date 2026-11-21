import heapq
import re
from collections import deque
from itertools import count
from typing import Callable, Hashable, Iterable, Iterator

def get_input_lines(filename:str) -> list:
    input = open(filename, 'r')
    return [line.strip() for line in input.readlines()]

def get_input_lines_as_grid(filename:str) -> list:
    input = open(filename, 'r')
    return [list(line.strip()) for line in input.readlines()]

def grid_get(grid:list, row: int, col: int, default:str='.') -> str:
    if row < 0 or col < 0:
        return default
    try:
        return grid[row][col]
    except IndexError:
        return default
    
def print_grid(data:list):
    for line in data:
        print(' '.join([str(item) if len(str(item)) > 1 else ' ' + str(item) for item in line]))

def print_list(data:list, limit:int=80):
    printable = ''
    for item in data:
        printable += str(item)
        if len(printable) > limit:
            break
    print(printable)

def replace_char_at(string:str, index:int, replacement:str) -> str:
    return string[:index] + replacement + string[index + 1:]

DIRS4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIRS8 = DIRS4 + [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def ints(line:str) -> list[int]:
    return [int(n) for n in re.findall(r'-?\d+', line)]

def in_bounds(grid:list, row:int, col:int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])

def neighbors(grid:list, row:int, col:int, dirs:list=DIRS4) -> Iterator[tuple[int, int]]:
    for drow, dcol in dirs:
        if in_bounds(grid, row + drow, col + dcol):
            yield row + drow, col + dcol

def bfs(start:Hashable, next_states:Callable) -> dict:
    """Steps from start to every reachable state. next_states(state) yields neighbor states."""
    dist = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for nxt in next_states(state):
            if nxt not in dist:
                dist[nxt] = dist[state] + 1
                queue.append(nxt)
    return dist

def dijkstra(start:Hashable, next_states:Callable) -> dict:
    """Lowest cost from start to every reachable state. next_states(state) yields (neighbor, cost)."""
    dist = {start: 0}
    tiebreak = count()
    heap = [(0, next(tiebreak), start)]
    while heap:
        cost, _, state = heapq.heappop(heap)
        if cost > dist[state]:
            continue
        for nxt, step in next_states(state):
            new_cost = cost + step
            if nxt not in dist or new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(heap, (new_cost, next(tiebreak), nxt))
    return dist
