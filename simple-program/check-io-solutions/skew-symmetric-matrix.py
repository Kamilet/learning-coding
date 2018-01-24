'''
求一个矩阵是否和共轭矩阵+负号相等
'''

# in using sMartix
# https://github.com/Kamilet/Simple-Matrix-python
# From --------------------------------------

def sm_trans(matrix):
    '''Transpose'''
    _row, _colume = sm_check(matrix)
    new_matrix = sm_gen(_colume,_row)
    for _r in range(_row):
        for _c in range(_colume):
            new_matrix[_c][_r] = matrix[_r][_c]
    return new_matrix


def sm_copy(matrix):
    '''perform a deep copy for matrix'''
    _row = len(matrix)
    _colume = len(matrix[0])
    new_matrix = sm_gen(_row, _colume)
    for _r in range(_row):
        for _c in range(_colume):
            new_matrix[_r][_c] = matrix[_r][_c]
    return new_matrix


def sm_check(matrix):
    '''Check if the row and colume >=1
    Check if all row has same length'''
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


def sm_numcheck(matrix):
    '''Check is matrix is legal.
    And all items must be number.'''
    if not sm_check(matrix):
        return False
    _colume = len(matrix[0])
    for items in matrix:
        for _c in range(_colume):
            try:
                _temp = eval(str(items[_c]))
            except NameError:
                return False
            except TypeError:  # new for plural, wrong input will cause Eror
                pass
    return True


def sm_number(matrix, force=False):
    '''set every numbers to numbertype
    set force=True will replace letters and '' with 0'''
    new_matrix = sm_copy(matrix)
    for _r in range(len(new_matrix)):
        for _c in range((len(new_matrix[0]))):
            try:
                new_matrix[_r][_c] = eval(str(new_matrix[_r][_c]))
            except NameError:
                assert force, 'Error: Your matrix is not all numbers!\n\
You can try to use force=True for argument in function like:sm_number(matrix, force).'
                new_matrix[_r][_c] = 0
            except TypeError:  # new for plural, wrong input will cause Eror
                pass
    return new_matrix


def sm_negative(matrix):
    '''Set every numbers to -(number)'''
    if sm_numcheck(matrix):
        new_matrix = sm_copy(matrix)
        new_matrix = sm_number(new_matrix)
        for _r in range(len(new_matrix)):
            for _c in range((len(new_matrix[0]))):
                new_matrix[_r][_c] *= -1
        return new_matrix
    else:
        assert False, 'Error: Your matrix is not all numbers'


def sm_gen(row: int = 1, colume: int = 1, items=0, unit=False, eye=False):
    '''Generate a matrix with row and colume,
    items can be numbers or string (can't calculate)
    set unit=True or eye=True to generate a unit matrix with row: sm_gen(row, eye=True)'''
    if unit or eye:
        matrix = sm_gen(row, row, items=0)
        for i in range(row):
            matrix[i][i] = 1
    else:
        matrix = [None] * row
        for _r in range(row):
            matrix[_r] = [items] * colume
    return matrix
# End --------------------------------------


def checkio(matrix):
    return matrix == sm_negative(sm_trans(matrix))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
