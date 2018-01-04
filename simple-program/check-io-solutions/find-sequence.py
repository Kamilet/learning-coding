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
    for colume in range(N-3):
        # from [0,0] to [n-3][n-3], line++, colume++
        for line in range(N-3):
            if matrix[line][colume] == matrix[line+1][colume+1]\
            and matrix[line][colume] == matrix[line+2][colume+2]\
            and matrix[line][colume] == matrix[line+3][colume+3]:
                return True
        # from [0,3] to [n-3,0], line--, colume++ (contrast to the axes)
        for line in range(3,N):
            if matrix[line][colume] == matrix[line+1][colume-1]\
            and matrix[line][colume] == matrix[line+2][colume-2]\
            and matrix[line][colume] == matrix[line+3][colume-3]:
                return True
        # from [0,0] to [n, n-3], colume ++ (contrast to the axes)
        for line in range(0,N-3):
            if matrix[line][colume] == matrix[line+1][colume]\
            and matrix[line][colume] == matrix[line+2][colume]\
            and matrix[line][colume] == matrix[line+3][colume]:
                return True
        #
            if matrix[colume][line] == matrix[colume][line]\
            and matrix[colume][line] == matrix[colume][line]\
            and matrix[colume][line] == matrix[colume][line]:
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
