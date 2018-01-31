'''
求矩阵的行列式
'''


def checkio(m):
    if len(m) == 1:
        return m[0][0]
    else:
        s = 0
        for i in range(len(m)):
            n = [[row[a] for a in range(len(m)) if a != i] for row in m[1:]]
            s += m[0][i] * checkio(n) * (-1) ** (i % 2)
        return s


checkio([[4, 3], [6, 3]]) == -6
checkio([[1, 3, 2],
         [1, 1, 4],
         [2, 2, 1]]) == 14
a = checkio([[2, 7, 6, 4, 2, 0], [3, 0, 8, 2, 5, 6], [3, 8, 9, 1, 0, 3], [
            9, 4, 5, 0, 8, 6], [8, 9, 0, 6, 4, 6], [1, 6, 3, 0, 7, 1]])
print(a)  # -140558

'''
# 有问题，待修复

# Using sMartix ---------------------------------
# https://github.com/Kamilet/Simple-Matrix-python

def sm_det(matrix, force=False):
    _row, _colume = sm_check(matrix)
    _det = 0
    if _row == 2:
        _det = matrix[1][1] * matrix[0][0] - matrix[0][1] * matrix[1][0]
        return _det
    for _r in range(_colume):
        _temp1 = 1
        _temp2 = 1
        for _c in range(_row):
            _temp1 *= matrix[_c][(_r+_c)%_colume]
            _temp2 *= matrix[_c][(_r-_c)%_colume]
        _det = _det + _temp1 - _temp2
    return _det


def sm_check(matrix):
    try:
        _row = len(matrix)
        _colume = len(matrix[0])
        if _colume:
            for items in matrix:
                if len(items) != _colume:
                    return False
            return _row, _colume
        else:
            return False
    except IndexError:
        return False

# End ----------------------------
'''1
