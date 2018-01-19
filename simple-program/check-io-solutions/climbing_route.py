'''
爬山问题。
给一个地图，数字是高度。
必须从高度1开始往上爬，每次最多只能上1个高度。
从左上开始，到右下，必须经过每个山头。
求最短路径。
https://py.checkio.org/mission/climbing-route/
暂时没思路……
'''

'''
未解决，未提交
'''

'''
大神的解法，分析中
'''

from math import inf
from itertools import permutations
 
def get_neighbors(fun, nrow, ncol, r, c):
    for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        rr = r + dr
        cc = c + dc
        if 0 <= rr < nrow and 0 <= cc < ncol:
            if fun(r, c, rr, cc):
                yield (rr, cc)
 
def get_mountains(emap, nrow, ncol):
    hills = [(r, c) for r in range(nrow) for c in range(ncol) if emap[r][c] > 0]
    is_hill = lambda r, c, rr, cc: emap[rr][cc] > 0
    while hills:
        adjacent = []
        to_visit = [hills[0]]
        while to_visit:
            rc = to_visit.pop()
            if rc in hills:
                hills.remove(rc)
                r, c = rc
                adjacent.append((emap[r][c], rc))
                for pos in get_neighbors(is_hill, nrow, ncol, r, c):
                    if pos in hills:
                        to_visit.append(pos)
        adjacent.sort()
        if len(adjacent) > 1 and adjacent[-2][0] != adjacent[-1][0]:
            yield adjacent[-1][1]
 
def reconstruct_path(path, current):
    route = [current]
    while current in path:
        current = path[current]
        route.append(current)
    return route
 
class SearchPathCache:
 
    def __init__(self, fun):
        self.fun = fun
        self.cache = {}
 
    def __call__(self, emap, nrow, ncol, start, end):
        key = (start, end)
        if key not in self.cache:
            self.cache[key] = self.fun(emap, nrow, ncol, start, end)
        return self.cache[key]
 
@SearchPathCache
def search_path(emap, nrow, ncol, start, end):
    # Pseudo A* algorithm
    passable = lambda r, c, rr, cc: abs(emap[r][c] - emap[rr][cc]) < 2
 
    opened = [start]    # nodes discovered but not evaluated
    closed = []         # nodes already evaluated
    cost = {start: 0}   # cost of getting from the start node to that node
    path = {}           # travelling of nodes
 
    while opened:
        min_cost = sorted((cost[i], i) for i in opened if i in cost)
        if min_cost:
            current = min_cost[0][1]
        else:
            current = opened[0]
 
        opened.remove(current)
        closed.append(current)
 
        if current == end:
            return reconstruct_path(path, current)
 
        for neighbor in get_neighbors(passable, nrow, ncol, *current):
 
            if neighbor in closed:
                continue
 
            if neighbor not in opened:
                opened.append(neighbor)
 
            tentative = cost[current] + 1
            if neighbor in cost and tentative >= cost[neighbor]:
                continue
 
            path[neighbor] = current
            cost[neighbor] = tentative
 
def climbing_route(elevation_map):
    emap = tuple(tuple(map(int, row)) for row in elevation_map)
    nrow = len(emap)
    ncol = len(emap[0])
    start = (0, 0)
    end = (nrow - 1, ncol - 1)
    mountains = list(get_mountains(emap, nrow, ncol))
    search_path.cache.clear()
    min_steps = inf
    for objectives in permutations(mountains, len(mountains)):
        steps = 0
        a = start
        for b in (*objectives, end):
            path = search_path(emap, nrow, ncol, a, b)            
            if path:
                steps += (len(path) - 1)
                if steps >= min_steps:
                    steps = 0
                    break
                a = b
            else:
                steps = 0
                break
        if steps and steps < min_steps:
            min_steps = steps
    return min_steps


if __name__ == '__main__':
    assert climbing_route([
        '0000',
        '0210',
        '0000']) == 7, 'basic'

    assert climbing_route([
        '00000',
        '03440',
        '03650',
        '02210',
        '00000']) == 26, 'spiral'

    assert climbing_route([
        '000000001',
        '222232222',
        '100000000']) == 26, 'bridge'

    assert climbing_route([
        '000000001210',
        '011100002320',
        '012100001210',
        '011100000000']) == 16, 'two top'

    assert climbing_route([
        '00000000000000',
        '01212321234320',
        '00000000000000']) == 21, 'one top'

    assert climbing_route([
        '00000000000000000000000000',
        '00000000000111111100000000',
        '00000000000122222100000000',
        '00000000000123332100000000',
        '00000000000123432100000000',
        '00000000000123332100000000',
        '00000000000122222100000000',
        '00000000000111111100000000',
        '00000000000000000000000000',
        '00000111110000000000000000',
        '00000122210000000000000000',
        '00000123210000000000000000',
        '00000122210000000011223110',
        '00000111110000000000000000',
        '01110000000000000000000000',
        '01210000000000000000000000',
        '01110000000000000000000000',
        '00000000000000000000000000']) == 70, 'pyramids'