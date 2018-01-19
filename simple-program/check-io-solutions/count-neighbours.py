'''
本质上就是扫雷……判断周围方格有几个。  
判断边界懒得写……给grid外面加一圈0，然后直接暴力输出。
'''
def count_neighbours(grid, row, col):
    lenth_row = len(grid)
    lenth_col = len(grid[0])
    new_grid = []
    for r in grid:
        new_grid.append([0]+list(r)+[0])
    new_grid = [[0]*(lenth_col+2)] + new_grid + [[0]*(lenth_col+2)]
    count = 0
    for i in [0,1,2]:
        for k in [0,1,2]:
            count+=new_grid[row+i][col+k]
    return count-new_grid[row+1][col+1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
