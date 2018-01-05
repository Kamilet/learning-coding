###########################################################
# 目标是写出一个包含各种函数的py文件，能承担简单的矩阵运算。
# 命名为sMartix，是Simple matrix的意思，复杂功能的不考虑。
# 计划开始于  |  Kamilet 2018-01-05  |  coding.kamilet.cn
###########################################################
# 个人很讨厌矩阵，这也是为什么我打算写一个矩阵的拓展自己用。
# 仅处理二维矩阵的基本运算，并附带检查和生成矩阵的功能。
# 起码要包括高数常用的功能，并希望包括查询功能（五子棋）。


def m_gen(row:int = 1, colume:int = 1, items = 0):
    '''Generate a matrix with row and colume,
    items can be numbers or string (can't calculate)'''
    # 生成一个矩阵，可以设置行列以及默认填充的元素
    # 默认1行，1列，填充数字0
    # 返回元组
    return [[items] * colume] * row


def m_cons(matrix, items = 0, echo = 0):
    '''Construct a matrix, for example:
    if matrix is [[1,2],[1]], would return [[1,2],[1,items]]
    the first row and column must exist
    and any item like '' will be items'''
    # 建设一个矩阵，填充任何列数不足第一行列数的行
    # 空元素会被填充成items
    if echo: print('Your matrix will be full filled by:',items)
    _row = len(matrix[0])
    _column = len(matrix)
    for r in range(0, _column):
        for c in range(0, _row):
            try:
                if matrix[r][c] == '':
                    matrix[r][c] = items
            except:
                matrix[r].append(items)
    return matrix


def m_numCheck(matrix):
    '''Check is matrix is legal.
    And all items must be number.'''
    # 检查一个矩阵是否合法，并检查是否所有都是数字
    if not m_check(matrix):
        return False
    _column = len(matrix[0])
    for items in matrix:
        for c in range(_column):
            if not str(items[c]).isdigit():
                return False
    return True


def m_check(matrix):
    '''Check if the row and column >=1
    Check if all row has same length'''
    # 检查矩阵是否合法，返回行列数，否则返回False
    # 此处不检查是否是数字
    try:
        _row = len(matrix)
        _column = len(matrix[0])
        if _row and _column:
            for items in matrix:
                if len(items) != _row:
                    return False
            return _row, _column
        else:
            return False
    except:
        return False


# 用于对单一矩阵进行处理
class Smatrix:
    def __init__(self, matrix, allnumber = False):
        '''an error check will run automaticlly'''
        self.matrix = matrix
        _check = m_check(matrix)
        if _check:
            self.row = _check[1]
            self.colume = _check[0]
        else:
            assert False, 'Error: Your matrix is illegal'
        if allnumber and not m_numCheck(matrix):
            assert False, 'Error: Your matrix is illegal'



    def clean(self, items = 0, echo = False):
        '''clear a matrix with 0 as defult'''
        # 默认情况下，用0填充整个矩阵
        if echo: print('Your items in matrix has been replaced with:',items)
        return m_gen(self.row, self.colume, items)


    def rotate(method = exchange, step:int = 1):
        '''rotate a matrix, set strp to act serveral tiems, set method to:
        - exchange:(or ex) exchange rows and columes
        - clockwise:(or clock) rotate it in clockwise
        - mirrorrow:(or mr | or mv) mirror in horizontal direction
        - mirrorcolume:(or mc | or mv) mirror in vertical'''





# Testing
a = [[1,2],[1,0]]
b = Smatrix(a).clean(echo = 1)
c = [[1,3,4],[2,'']]

m_check(a)
print(m_numCheck(a))
print(a)
print(b)
print(m_cons(c,echo=1))