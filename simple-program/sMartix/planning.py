'''
A lightweight module for handling matrices
'''

###########################################################
# 目标是写出一个包含各种函数的py文件，能承担简单的矩阵运算。
# 命名为sMartix，是Simple matrix的意思，复杂功能的不考虑。
# 计划开始于  |  Kamilet 2018-01-05  |  coding.kamilet.cn
###########################################################
# 个人很讨厌矩阵，这也是为什么我打算写一个矩阵的拓展自己用。
# 仅处理二维矩阵的基本运算，并附带检查和生成矩阵的功能。
# 起码要包括高数常用的功能，并希望包括查询功能（五子棋）。

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2018-01-05

# -------------------------------------------------------
# Handle with single matrix
# -------------------------------------------------------


def sm_gen(row: int = 1, colume: int = 1, items=0):
    '''Generate a matrix with row and colume,
    items can be numbers or string (can't calculate)'''
    # 生成一个矩阵，可以设置行列以及默认填充的元素
    # 默认1行，1列，填充数字0
    # 返回元组
    matrix = [None] * row
    for _r in range(row):
        matrix[_r] = [items] * colume
    return matrix


def sm_cons(matrix, items=0, echo=0):
    '''Construct a matrix, for example:
    if matrix is [[1,2],[1]], would return [[1,2],[1,items]]
    the first row and colume must exist
    and any item like '' will be items'''
    # 建设一个矩阵，填充任何列数不足第一行列数的行
    # 空元素会被填充成items
    if echo:
        print('Your matrix will be full filled by:', items)
    _row = len(matrix[0])
    _colume = len(matrix)
    for _r in range(0, _colume):
        for _c in range(0, _row):
            try:
                if matrix[_r][_c] == '':
                    matrix[_r][_c] = items
            except:
                matrix[_r].append(items)
    return matrix


def sm_numcheck(matrix):
    '''Check is matrix is legal.
    And all items must be number.'''
    # 检查一个矩阵是否合法，并检查是否所有都是数字
    if not sm_check(matrix):
        return False
    _colume = len(matrix[0])
    for items in matrix:
        for _c in range(_colume):
            try:
                _temp = eval(str(items[_c]))
            except NameError:
                return False
    return True


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


def sm_negative(matrix):
    '''Set every numbers to -(number)'''
    # 给所有数加一个负号
    if sm_numcheck(matrix):
        matrix = sm_number(matrix)
        for _r in range(len(matrix)):
            for _c in range((len(matrix[9]))):
                matrix[_r][_c] *= -1
        return matrix
    else:
        assert False, 'Error: Your matrix is not all numbers'


def sm_abs(matrix):
    '''set every numbers to abs(number)'''
    # 将所有数据绝对值化
    if sm_numcheck(matrix):
        matrix = sm_number(matrix)
        for _r in range(len(matrix)):
            for _c in range((len(matrix[0]))):
                matrix[_r][_c] = abs(matrix[_r][_c])
        return matrix
    else:
        assert False, 'Error: Your matrix is not all numbers'


def sm_number(matrix, force=False):
    '''set every numbers to numbertype
    set force=True will replace alphabate and '' with 0'''
    # 将所有数据数值化
    # 将force设置为True将使得所有非字母转化为0
    for _r in range(len(matrix)):
        for _c in range((len(matrix[0]))):
            try:
                matrix[_r][_c] = eval(str(matrix[_r][_c]))
            except NameError:
                assert force, 'Error: Your matrix is not all numbers!\n\
You can try to use force=True for argument in function sm_number(matrix, force).'
                matrix[_r][_c] = 0
    return matrix


class Smatrix:
    '''handdel a single matrix'''
    # 用于对单一矩阵进行处理

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

    def clean(self, items=0, echo=False):
        '''clear a matrix with 0 as defult'''
        # 默认情况下，用0填充整个矩阵
        if echo:
            print('Your items in matrix has been replaced with:', items)
        return sm_gen(self.row, self.colume, items)

    def check(self):
        '''Check if the row and colume >=1
        Check if all row has same length'''
        # 检查矩阵是否合法，返回行列数，否则返回False
        # 此处不检查是否是数字
        return sm_check(self.matrix)

    def numcheck(self):
        '''Check is matrix is legal.
        And all items must be number.'''
        # 检查一个矩阵是否合法，并检查是否所有都是数字
        return sm_numcheck

    def view(self):
        '''view the matrix'''
        for item in self.matrix:
            print(item)

    def rotate(self, method='exchange', step: int=1, force=False):
        '''rotate a matrix, set strp to act serveral tiems, set method to:
        - exchange:(or ex) exchange rows and columes
        - clockwise:(or clock) rotate it in clockwise
        - mirrorrow:(or mr | or mh | or mirror) mirror in horizontal direction
        - mirrorcolume:(or mc | or mv) mirror in vertical
        set force=True will assert Error when no opreation happened'''
        # 矩阵的旋转翻转操作：
        # ex - 横纵交换，clock - 顺时针旋转， mh-水平翻转， mv - 垂直翻转
        new_matrix = self.matrix
        if method == 'exchange' or method == 'ex':
            step %= 2
            while step:
                step -= 1
                new_matrix = sm_gen(self.colume, self.row, '')
                # _row and _colume here for new_matrix
                for _row in range(self.colume):
                    for _colume in range(self.row):
                        print(new_matrix)
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
        elif method == 'mirrorrow' or method == 'mr' or\
                method == 'mh' or method == 'mirror':
            step %= 2
            while step:
                step -= 1
                for _row in range(self.row):
                    new_matrix[_row] = new_matrix[_row][::-1]
        elif method == 'mirrorcolume' or method == 'mc' or method == 'mv':
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


# -------------------------------------------------------
# Handle with multiple matrixs
# -------------------------------------------------------


def sm_sum(*matrixs, force=False):
    ''' sum all given matrixs
    set force=True to ignore '' and alphabates
    use sm_negative() to minus anyone'''
    # 矩阵求和，设置force为True可以强制字母和空字符被作为0求和
    _row = len(matrixs[0])
    _colume = len(matrixs[0][0])
    for _item in matrixs[1:]:
        if len(_item) != _row or len(_item[0]) != _colume:
            assert False, 'Cannot sum matrixs with different numbers of rows or columes!'


# Testing
'''
a = [[1, 2], [1, 0]]
b = Smatrix(a).clean(echo=1)
c = [[1, 3, 4], [2, '']]
d = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]

sm_check(a)
print(sm_numcheck(a))
print(a)
print(b)
print(sm_cons(c, echo=1))
e = Smatrix(d)
e.view()
e = e.rotate('mirrorcolume')
e = Smatrix(e)
e.view()
print(help(Smatrix))


print(sm_numcheck([['A',1],[1,2]]))
print(sm_numcheck([['1',1],[1,2]]))
print(sm_numcheck([[1,1.321],[1,2]]))

print(sm_number([['A',1],[1,2]], force = 1))
print(sm_number([['1',1],[1,2]]))
print(sm_number([[1,1.321],[1,2]]))
'''