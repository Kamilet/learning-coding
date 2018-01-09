'''
对位密码表
向右翻转3次
'''

# --------- form sMartix ----------
# https://github.com/Kamilet/learning-coding/tree/master/simple-program/sMartix/sMartix.py


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
    # 检查矩阵是否合法，返回行列数，否则返回False
    # 此处不检查是否是数字
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


class Smatrix:
    '''handdel a single matrix'''

    def __init__(self, matrix, allnumber=False):
        '''an error check will run automaticlly'''
        self.matrix = matrix
        _check = sm_check(matrix)
        if _check:
            self.colume = _check[1]  # len(matrix)
            self.row = _check[0]  # len(matrix[0])
        else:
            assert False, 'Error: Your matrix is illegal'
        if allnumber and not sm_numcheck(matrix):
            assert False, 'Error: Your matrix is illegal'

    def rotate(self, method='exchange', step: int=1, force=False):
        '''rotate a matrix, set strp to act serveral tiems, set method to:
        - transpose:(or exchange | or ex | or tr) exchange rows and columes
        - clockwise:(or clock) rotate it in clockwise
        - mirrorrow:(or mr | or mh | or mirror) mirror in horizontal direction
        - mirrorcolume:(or mc | or mv) mirror in vertical
        set force=True will assert Error when no opreation happened'''
        new_matrix = sm_copy(self.matrix)
        if method in ['transpose', 'exchange', 'ex', 'tr']:
            step %= 2
            while step:
                step -= 1
                new_matrix = sm_gen(self.colume, self.row, '')
                # _row and _colume here for new_matrix
                for _row in range(self.colume):
                    for _colume in range(self.row):
                        new_matrix[_row][_colume] = self.matrix[_colume][_row]
        elif method == 'clockwise' or method == 'clock':
            step %= 4
            while step:
                step -= 1
                o_colume = len(new_matrix[0])
                o_row = len(new_matrix)
                o_matrix = new_matrix
                new_matrix = sm_gen(o_colume, o_row, '')
                for _row in range(o_colume):
                    for _colume in range(o_row):
                        new_matrix[_row][_colume] = o_matrix[
                            o_row - _colume - 1][_row]
        elif method in ['mirrorrow', 'mr', 'mh', 'mirror']:
            step %= 2
            while step:
                step -= 1
                for _row in range(self.row):
                    new_matrix[_row] = new_matrix[_row][::-1]
        elif method in ['mirrorcolume', 'mc', 'mv']:
            step %= 2
            while step:
                step -= 1
                for line in range(0, self.row // 2):
                    new_matrix[line], new_matrix[self.row - line - 1] =\
                        new_matrix[self.row - line - 1], new_matrix[line]
        elif force:
            assert False, 'Error: rotate(method={}, step={})'.format(
                method, step)
        return new_matrix

# --------- sMartix ----------


def recall_password(cipher_grille, ciphered_password):
    password = []
    password_matrix = sm_gen(4, 4)
    for i in [0, 1, 2, 3]:
        for k in [0, 1, 2, 3]:
            password_matrix[i][k] = cipher_grille[i][k]

    for turn in [0, 1, 2, 3]:
        for i in [0, 1, 2, 3]:
            for k in [0, 1, 2, 3]:
                if password_matrix[i][k] == 'X':
                    password.append(ciphered_password[i][k])
        password_matrix = Smatrix(password_matrix)
        password_matrix = password_matrix.rotate(method = 'clockwise')

    return ''.join(password)


# ---------------------------------


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing


    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

'''
def recall_password(cipher_grille, ciphered_password):
    password = [[],[],[],[]]
    cipher_grille = list(cipher_grille)
    ciphered_password = list(ciphered_password)
    for i in [0,1,2,3]:
        for k in [0,1,2,3]:
            if cipher_grille[i][k] == 'X':
                password[0].append(ciphered_password[i][k])
                password[2].append(ciphered_password[3-i][3-k])

    for i in [0,1,2,3]:
        for k in [3,2,1,0]:
            if cipher_grille[i][k] == 'X':
                password[1].append(ciphered_password[k][3-i])
                password[3].append(ciphered_password[3-k][i])
    password[1] = password[1][1:4] + [password[1][0]]
    password[3] = [password[3][0]] + password[3][3:0:-1]
    print(password[1],'!!!')
    print(password[3],'!!!')

    print(''.join(password[0]+password[1]+password[2][::-1]+password[3]))
    return ''.join(password[0]+password[1]+password[2][::-1]+password[3])

'''
