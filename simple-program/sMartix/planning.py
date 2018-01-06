'''
A lightweight module for handling Real Number Matrix.
Plural actually available, but complete test haven't done...
All items should be numbers or letters in matrix.
Please use Numpy for more complex situation!
'''

###########################################################
# 目标是写出一个包含各种函数的py文件，进行简单的实数矩阵运算。
# 命名为sMartix，是Simple matrix的意思，简单处理简单矩阵。
# 计划开始于  |  Kamilet 2018-01-05  |  coding.kamilet.cn
###########################################################
# 个人很讨厌矩阵，这也是为什么我打算写一个矩阵的拓展自己用。
# 仅处理二维矩阵的基本运算，并附带检查和生成矩阵的功能。
# 起码要包括高数常用的功能，并希望包括查询功能（五子棋）。
# 只对元素为单个数字的矩阵进行处理，复杂的为什么不用Numpy？
# 尝试加入复数，测试中

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '0.8a'  # lastchanged: 2018-01-06

# -------------------------------------------------------
# Handle with single matrix
# -------------------------------------------------------


def sm_gen(row: int = 1, colume: int = 1, items=0, unit=False, eye=False):
    '''Generate a matrix with row and colume,
    items can be numbers or string (can't calculate)
    set unit=True or eye=True to generate a unit matrix with row: sm_gen(row, eye=True)'''
    # 生成一个矩阵，可以设置行列以及默认填充的元素
    # 默认1行，1列，填充数字0
    # 设置unit为True会生成单位矩阵，根据row
    if unit or eye:
        matrix = sm_gen(row, row, items=0)
        for i in range(row):
            matrix[i][i] = 1
    else:
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
    new_matrix = sm_copy(matrix)
    if echo:
        print('Your matrix will be full filled by:', items)
    _row = len(new_matrix[0])
    _colume = len(new_matrix)
    for _r in range(0, _colume):
        for _c in range(0, _row):
            try:
                if new_matrix[_r][_c] == '':
                    new_matrix[_r][_c] = items
            except:
                new_matrix[_r].append(items)
    return new_matrix


def sm_copy(matrix):
    '''perform a deep copy for matrix'''
    # 深度拷贝！
    # 建议所有涉及矩阵直接整块赋值的情况都使用copy！
    # 拓展这个模块时，请确保所有的new_matrix都通过gen或copy生成！
    _row = len(matrix)
    _colume = len(matrix[0])
    new_matrix = sm_gen(_row, _colume)
    for _r in range(_row):
        for _c in range(_colume):
            new_matrix[_r][_c] = matrix[_r][_c]
    return new_matrix


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
            except TypeError:  # new for plural, wrong input will cause Eror
                pass
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
        new_matrix = sm_copy(matrix)
        new_matrix = sm_number(new_matrix)
        for _r in range(len(new_matrix)):
            for _c in range((len(new_matrix[0]))):
                new_matrix[_r][_c] *= -1
        return new_matrix
    else:
        assert False, 'Error: Your matrix is not all numbers'


def sm_abs(matrix):
    '''set every numbers to abs(number)'''
    # 将所有数据绝对值化
    if sm_numcheck(matrix):
        new_matrix = sm_copy(matrix)
        new_matrix = sm_number(new_matrix)
        for _r in range(len(new_matrix)):
            for _c in range((len(new_matrix[0]))):
                new_matrix[_r][_c] = abs(new_matrix[_r][_c])
        return new_matrix
    else:
        assert False, 'Error: Your matrix is not all numbers'


def sm_number(matrix, force=False):
    '''set every numbers to numbertype
    set force=True will replace letters and '' with 0'''
    # 将所有数据数值化
    # 将force设置为True将使得所有非字母转化为0
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


def sm_str(matrix):
    '''set every items to string type'''
    # 将所有数据字符化
    new_matrix = sm_copy(matrix)
    for _r in range(len(new_matrix)):
        for _c in range((len(new_matrix[0]))):
            new_matrix[_r][_c] = str(new_matrix[_r][_c])
    return new_matrix


def sm_trans(matrix):
    '''Transpose'''
    # 单独的转置函数
    _row, _colume = sm_check(matrix)
    new_matrix = sm_gen(_colume,_row)
    for _r in range(_row):
        for _c in range(_colume):
            new_matrix[_c][_r] = matrix[_r][_c]
    return new_matrix


def sm_con_trans(matrix):
    '''Conjugation transpose'''
    # 复数的共轭转置
    _row, _colume = sm_check(matrix)
    new_matrix = sm_gen(_colume,_row)
    for _r in range(_row):
        for _c in range(_colume):
            if matrix[_r][_c].imag != 0:
                new_matrix[_c][_r] = matrix[_r][_c].real - matrix[_r][_c].imag * 1j
            else:
                new_matrix[_c][_r] = matrix[_r][_c].real
    return new_matrix


def sm_det(matrix, force=False):
    '''Determinant, return a number
    set force=True to calculate even row != column'''
    # 行列式运算，返回数值
    _row, _colume = sm_check(matrix)
    new_matrix = sm_number(sm_copy(matrix))
    _det = 0
    if not (force or _row == _colume) or not sm_numcheck(matrix):
        assert False, 'Error: Your matrix is illegal for Det(A)'
    for _r in range(_colume):
        _temp1 = 1
        _temp2 = 1
        for _c in range(_row):
            _temp1 *= new_matrix[_c][(_r+_c)%_colume]
            _temp2 *= new_matrix[_c][(_r-_c)%_colume]
        _det = _det + _temp1 - _temp2
    return _det


def sm_inverse(matrix):
    '''Inverse matrix'''
    # 求逆矩阵
    pass


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
        return sm_numcheck(self.matrix)

    def view(self):
        '''view the matrix'''
        # 将矩阵按照行列打印出来
        for item in self.matrix:
            print(item)

    def negative(self):
        '''Set every numbers to -(number)'''
        # 给所有数加一个负号
        return sm_negative(self.matrix)

    def rotate(self, method='exchange', step: int=1, force=False):
        '''rotate a matrix, set strp to act serveral tiems, set method to:
        - transpose:(or exchange | or ex | or tr) exchange rows and columes
        - clockwise:(or clock) rotate it in clockwise
        - mirrorrow:(or mr | or mh | or mirror) mirror in horizontal direction
        - mirrorcolume:(or mc | or mv) mirror in vertical
        set force=True will assert Error when no opreation happened'''
        # 矩阵的旋转翻转操作：
        # ex - 横纵交换，clock - 顺时针旋转， mh-水平翻转， mv - 垂直翻转
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

    def tran(self):
        '''transpose, same as rotate(matrix, transpose)'''
        # 单独的转置
        return sm_trans(self.matrix)

    def con_trans(self):
        '''Conjugation transpose, transpose for plural'''
        # 共轭转置
        return sm_con_trans(self.matrix)

    def det(self):
        '''Determinant'''
        # 行列式运算
        return sm_det(self.matrix)

    def inverse(self):
        '''Inverse matrix'''
        # 求逆矩阵
        return sm_inverse(self.matrix)

    def find(self, string:str='', length=2, direct='all', echo=False):
        '''scan the matrix and find a cut with given length.
        set string to:
        - any string: scan for it
        - '': scan for a cut in that length
        set direct to:
        - all:(as defult, or a) scan in every direction
        - row:(or r) only scan in row
        - colume:(or c) only scan in colume
        - rowcolume:(or cr, or rc) scan in row and colume
        - oblique:(or o) scan in oblique
        set echo to:
        - False:(as defult) will return True is exist
        - True: will return the first match as [row1,colume1]
                means the match start at [row1,colume1]
        about priority:
        from hight to low : row - colume - oblique(\) - oblique(/)
        from [0,0] to [m-1,n-1]
        '''
        # 扫描系统，寻找长度匹配的切片，即“五子棋”系统
        # direct可以设置扫描方向：
        # all - 全局扫描；r - 只扫行内；c - 只扫列内；rc - 只扫行列；o - 只扫斜向
        # echo可以设置返回值：
        # False - 返回是否存在这样的切片；True - 返回匹配到第一个切片的起点
        # 检查优先级：行、列、左上到右下、右上到左下
        # 返还优先级：左到右，上到下
        # --
        # 不加这么多参数可以大大提高循环的效率的…
        # 比如行、列、斜和反斜可以共用第一个循环，行和列可以共用第二个循环
        string = str(string)
        _row = len(self.matrix)
        _colume = len(self.matrix[0])
        new_matrix = sm_str(self.matrix)
        if (_row < length and direct in ['all','a','row','r','oblique','o','rc','cr'])\
           or (_colume < length and direct in ['all','a','colume','c','oblique','o','rc','cr']):
            assert False, 'Length of cut cannot longer than length of scan area!'
        if direct in ['all','a','row','r','rc','cr']:
            # scan in row
            # 纯行扫描
            for _r in range(_row):
                for _scan in range(_colume - length + 1):
                    if string != '' and string != new_matrix[_r][_scan]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r][_scan:_scan+length][_i] != new_matrix[_r][_scan]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r,_scan
                        else:
                            return True
        if direct in ['all','a','colume','c','rc','cr']:
            # scan in colume
            # 纯列扫描
            for _r in range(_row - length + 1):
                for _scan in range(_colume):
                    if string != '' and string != new_matrix[_r][_scan]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r + _i][_scan] != new_matrix[_r - 1][_scan]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r,_scan
                        else:
                            return True
        if direct in ['all', 'a', 'oblique', 'o']:
            # scan in oblique
            # 斜向扫描
            # direction \ first
            for _r in range(_row - length +1):
                for _c in range(_colume - length + 1):
                    if string != '' and string != new_matrix[_r][_c]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r + _i][_c + _i] != new_matrix[_r][_c]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r,_c
                        else:
                            return True
            # direction / second
            # sure can put \ and / in same cycle, but too hard to read
            # especially when we need check flag and echo
            for _r in range(_row - length +1):
                for _c in range(length - 1, _colume):
                    if string != '' and string != new_matrix[_r][_c]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r + _i][_c - _i] != new_matrix[_r][_c]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r,_c
                        else:
                            return True
        return False

    def trace(self):
        '''return the trace, only for square matrix'''
        # 返回矩阵的迹，只对方阵有效
        _trace = 0
        sm_numcheck(self.matrix)
        for _cr in range(len(self.matrix)):
            trace += self.matrix[_cr][_cr]
        return trace



# -------------------------------------------------------
# Handle with multiple matrixs
# -------------------------------------------------------


def sm_sum(*matrixs, force=False):
    ''' sum all given matrixs
    set force=True to ignore '' and letters
    use sm_negative() to minus anyone'''
    # 矩阵求和，设置force为True可以强制字母和空字符被作为0求和
    _row = len(matrixs[0])
    _colume = len(matrixs[0][0])
    new_matrix = sm_number(matrixs[0], force)
    for _item in matrixs[1:]:
        if len(_item) != _row or len(_item[0]) != _colume:
            assert False, 'Cannot sum matrixs with different numbers of rows or columes!'
        _item = sm_number(_item, force)
        for _r in range(_row):
            for _c in range(_colume):
                new_matrix[_r][_c] += _item[_r][_c]
    return new_matrix


def sm_minus(matrix_1, matrix_2, force=False):
    '''minus two matrixs, matrix_1 - matrix_2'''
    # 两个矩阵相减，前减后
    return sm_copy(sm_sum(matrix_1, sm_negative(matrix_2), force=force))


def sm_multis(*matrixs_or_numbers, force=False):
    '''multiplication for matrixs and numbers'''
    # 矩阵的乘法或数乘
    matrixs = []
    numbers = 1
    for _item in matrixs_or_numbers:
        if type(_item) is list or type(_item) is tuple:
            if force:
                matrixs.append(sm_number(_item))
            elif sm_numcheck(_item):
                matrixs.append(_item)
            else:
                assert False, 'Your matrix is illegal for multiplication!'
        elif type(_item) is int or type(_item) is float or type(_item) is complex:
            # changed for plural
            numbers *= _item
        else: assert False, 'Type of arguments must be list or int or float or complex!'
    new_matrix = sm_copy(matrixs[0])
    for _i in range(1, len(matrixs)):
        new_matrix = sm_multi_mm(new_matrix, matrixs[_i])
    return sm_multi_mn(new_matrix, numbers)
        

def sm_multi_mm(matrix_1, matrix_2):
    '''multiplication for only 2 matrixs'''
    # 两个矩阵相乘
    _length = len(matrix_1[0])
    if _length != len(matrix_2):
        assert False, 'Your matrix is illegal for multiplication!'
    new_matrix = sm_gen(len(matrix_1), len(matrix_2[0]))
    for new_row in range(len(matrix_1)):
        for new_column in range(len(matrix_2[0])):
            for _n in range(_length):
                new_matrix[new_row][new_column] +=\
                matrix_1[new_row][_n] * matrix_2[_n][new_column]
    return new_matrix


def sm_multi_mn(matrix, number):
    '''multiplication for one matrix and one number'''
    # 矩阵和数字相乘
    new_matrix = sm_copy(matrix)
    for _item in new_matrix:
        for _i in range(len(_item)):
            _item[_i] *= number
    return new_matrix



'''
# Testing

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


a_1 = [[1,'A'],[1,1]]
a_2 = [[1, 1],[1,2]]
a_3 = [[1,'1'],[2,4]]
print(sm_minus(a_1,a_2,force = 1))

print(sm_gen(4,eye=1))
a = [[1, 2, 1, 5],
     [1, 2, 1, 4],
     [1, 1, 1, 6],
     [1, 7, 2, 5]]
A = Smatrix(a)
print('Start with',A.find('',2,'r',1),'in row')
print('Start with',A.find('',2,'c',1),'in colume')
print('Start with',A.find(1,3,'o',1),'in oblique')

mu1 = [[1,0,2],
       [-1,3,1]]

mu2 = [[3,1],
       [2,1],
       [1,0]]

mu3 = [[5,1],
       [2,2]]

print('矩阵1:')
Smatrix(mu1).view()
print('矩阵1，转置:')
temp = Smatrix(mu1).rotate()
Smatrix(temp).view()

print('矩阵1:')
Smatrix(mu1).view()
print('矩阵1+矩阵1:')
temp = sm_sum(mu1,mu1)
Smatrix(temp).view()

print('矩阵1:')
Smatrix(mu1).view()
print('矩阵2:')
Smatrix(mu2).view()
print('矩阵1 * 矩阵2:')
temp = sm_multis(mu1,mu2)
Smatrix(temp).view()
print('矩阵2 * 矩阵1:')
temp = sm_multis(mu2,mu1)
Smatrix(temp).view()
print('矩阵1 * 矩阵2 * 5:')
temp = sm_multis(mu1,5,mu2)
Smatrix(temp).view()

print('矩阵3:')
Smatrix(mu3).view()
print('矩阵1 * 矩阵2 * 矩阵3:')
temp = sm_multis(mu1,mu2,mu3)
Smatrix(temp).view()

print('矩阵1 * 矩阵3:前列后行不等报错')
temp = sm_multis(mu1,mu3)

mu4 = [[1,0,2],
       [-1,3,1]]
print(sm_trans(mu4))
m5 = [[(1+1j),(4-2j)],[4,(-1j)]]
print(sm_con_trans(m5))

'''
mu6 = [[1,1,1],
       [3,1,4],
       [8,9,5]]

mu7 = [[0,0,-1,0],
       [0,1,0,0],
       [-1,0,1,0]]

print(sm_det(mu6))
print(sm_det(mu7,force=1))
