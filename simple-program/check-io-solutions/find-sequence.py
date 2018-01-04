'''
给一个矩阵，找到连续的4个数字
和五子棋差不多吧
'''

'''
Analyze:
for a NxN(N>=4), we shold check:
    x[(0,N-3)][(0,N-3)] and 3 followers in line++ & colume++
    x[3,N][0,N-3] and 3 followers in line++ & colume--
    x[i][(0,N-3)] and 3 followers in line++
    x[(0,N-3)][i] and 3 followers in colume++

'''

def checkio(matrix):
    N = len(matrix)
    for x in range(N-3):
        # from [0,0] to [n-3][n-3], y++, x++
        for y in range(N-3):
            if matrix[y][x] == matrix[y+1][x+1]\
            and matrix[y][x] == matrix[y+2][x+2]\
            and matrix[y][x] == matrix[y+3][x+3]:
                return True
        # from [0,3] to [n-3,0], y--, x++ (contrast to the axes)
        for y in range(3,N):
            if matrix[y][x] == matrix[y-1][x+1]\
            and matrix[y][x] == matrix[y-2][x+2]\
            and matrix[y][x] == matrix[y-3][x+3]:
                return True
        # from [0,0] to [n, n-3], x ++ (contrast to the axes)
        for y in range(0,N):
            if matrix[y][x] == matrix[y][x+1]\
            and matrix[y][x] == matrix[y][x+2]\
            and matrix[y][x] == matrix[y][x+3]:
                return True
        #
            if matrix[x][y] == matrix[x+1][y]\
            and matrix[x][y] == matrix[x+2][y]\
            and matrix[x][y] == matrix[x+3][y]:
                return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([[2,6,2,2,7,6,5],[3,4,8,7,7,3,6],[6,7,3,1,2,4,1],[2,5,7,6,3,2,2],[3,4,3,2,7,5,6],[8,4,6,5,2,9,7],[5,8,3,1,3,7,8]]) == False, "Check"
