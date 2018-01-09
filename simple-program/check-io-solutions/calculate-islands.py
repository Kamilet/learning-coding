'''
数组内1代表岛屿，0代表水。
按顺序输出岛屿的大小
'''

def checkio(land_map):
    lands = []
    land = 0
    row = len(land_map)
    colume = len(land_map[0])
    for r in range(row):
        for c in range(colume):
            if land_map[r][c] == 1:
                lands.append(around(land_map,r,c))
    return sorted(lands)
    

def around(land_map, r, c, _lands=0):
    # force recursion, check around
    land_map[r][c] = 0
    _lands += 1
    try:
        if land_map[r-1][c] == 1 and r-1>=0:
            _lands = around(land_map, r-1, c, _lands)
    except: pass
    try:
        if land_map[r][c-1] == 1 and c-1>=0:
            _lands = around(land_map, r, c-1, _lands)
    except: pass
    try:
        if land_map[r+1][c] == 1:
            _lands = around(land_map, r+1, c, _lands)
    except: pass
    try:
        if land_map[r][c+1] == 1:
            _lands = around(land_map, r, c+1, _lands)
    except: pass
    try:
        if land_map[r-1][c+1] == 1 and r-1>=0:
            _lands = around(land_map, r-1, c+1, _lands)
    except: pass
    try:
        if land_map[r-1][c-1] == 1 and r-1>=0 and c-1>=0:
            _lands = around(land_map, r-1, c-1, _lands)
    except: pass
    try:
        if land_map[r+1][c-1] == 1 and c-1>=0:
            _lands = around(land_map, r+1, c-1, _lands)
    except: pass
    try:
        if land_map[r+1][c+1] == 1:
            _lands = around(land_map, r+1, c+1, _lands)
    except: pass
    return _lands



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
