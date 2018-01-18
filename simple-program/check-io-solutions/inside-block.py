'''
【此算法有BUG，改进算法在文末】
给定一组坐标，首尾相连形成一个多边形C。  
再给一个坐标，为点A。  
判断点A是否在多边形C内。  

### 算法原理：  
[百度百科，射线法]:(https://baike.baidu.com/item/%E5%B0%84%E7%BA%BF%E6%B3%95/22231858?fr=aladdin)  
引射线法：从目标点出发引一条射线，看这条射线和多边形所有边的交点数目。  
如果有奇数个交点，则说明在内部，如果有偶数个交点，则说明在外部。  

具体做法：将测试点的Y坐标与多边形的每一个点进行比较，  
会得到一个测试点所在的行与多边形边的交点的列表。

### 程序设计思路：
1. 判断点A是否在多边形C的顶点内，如果是，返回True。
2. 相邻两个一组提取点C的顶点(C1,C2)，如(C1,C2)的纵坐标一个大于C一个小于C，求和A画出水平线的交点，否则continue。
3. 交点和A重合，返回True；交点在A左侧，c_left+1；交点在A右侧，c_right+1。
4. 当c_left%2 == cright%2 == 1时，返回True，否则返回False。

### 其他：
思考的时候，就把第一个坐标当横坐标。  

## 问题：
之所以判断了左右，是因为想排除交点是顶点的情况。  
'''


def is_inside_bug(area, position):
    '''the position in given area ?'''
    # First test
    if position in area:
        return True
    # Check points once
    c_left = 0
    c_right = 0
    for ppp in range(-1, len(area)-1):
        first_point = area[ppp]
        second_point = area[ppp+1]
        if (first_point[1] >= position[1] and second_point[1] > position[1]) or\
           (first_point[1] <= position[1] and second_point[1] < position[1]):
            continue
        else:
            if first_point[0] == second_point[0]:
                cross_point_x = first_point[0]
            else:
                rate = (first_point[1] - second_point[1]) / \
                    (first_point[0] - second_point[0])
                plus = first_point[1] - first_point[0] * rate
                if rate:
                    cross_point_x = (position[1] - plus)/rate
                else:
                    if (first_point[0] >= position[0] and second_point[0] <= position[0]) or\
                       (first_point[0] <= position[0] and second_point[0] >= position[0]):
                        return True
                    else:
                        cross_point_x = first_point[0]
            if cross_point_x == position[0]:
                return True
            elif cross_point_x < position[0]:
                c_left += 1
            else:
                c_right += 1
    print(c_left, c_right)
    if c_left % 2 == 1 and c_right % 2 == 1:
        return True
    else:
        return False


# 改进算法
# 不算右，选择统计左边交点个数。
# 特殊判断：在交点是顶点的情况


def is_inside(area, position):
    '''the position in given area ?'''
    # First test
    if position in area:
        return True
    # Check points once
    c_left = []

    for ppp in range(-1, len(area)-1):
        first_point = area[ppp]
        second_point = area[ppp+1]
        if (first_point[1] > position[1] and second_point[1] > position[1]) or\
           (first_point[1] < position[1] and second_point[1] < position[1]):
            continue
        else:
            if first_point[0] == second_point[0]:
                cross_point_x = first_point[0]
            else:
                rate = (first_point[1] - second_point[1]) / \
                    (first_point[0] - second_point[0])
                plus = first_point[1] - first_point[0] * rate
                if rate:
                    cross_point_x = (position[1] - plus)/rate
                else:
                    if (first_point[0] >= position[0] and second_point[0] <= position[0]) or\
                       (first_point[0] <= position[0] and second_point[0] >= position[0]):
                        return True
                    else:
                        cross_point_x = first_point[0]
            if cross_point_x == position[0]:
                return True
            elif cross_point_x < position[0]:
                c_left.append((cross_point_x, position[1]))
    count_left = len(c_left)
    # print(c_left)
    # print(set(c_left))
    if count_left == len(set(c_left)):
        if count_left % 2 == 1:
            return True
        else:
            return False
    else:
        # 有重复元素，挑选出，找到相邻点，如果y不在同一侧就减去1
        Accuracy = 1/100
        while c_left:
            check_point = c_left.pop()
            if check_point in c_left:
                for i in range(len(area)):
                    if abs(area[i][0] - check_point[0]) < Accuracy and abs(area[i][1] - check_point[1]) < Accuracy:
                        if i+1 == len(area):
                            y1 = area[0][1]
                        else:
                            y1 = area[i+1][1]
                        y2 = area[i-1][1]
                        print(y1, y2, check_point, i)
                        if (y1 - position[1])*(y2 - position[1]) <= 0:
                            count_left -= 1
                        break
    if count_left % 2 == 1:
        return True
    else:
        # print(count_left)
        return False


if __name__ == '__main__':

    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2)) == True
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (4, 2)) == False
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"

    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"

    # checkio
    assert is_inside(((0, 0), (0, 2), (2, 2), (2, 0)), (1, 0)) == True
    assert is_inside(((1, 1), (1, 3), (2, 4), (4, 4),
                      (4, 3), (2, 1)), (3, 1)) == False
    # 在计算这一条时出现错误！

    assert is_inside(((0, 0), (1, 1), (2, 0), (3, 1),
                      (4, 0), (4, 2), (0, 2)), (2, 1)) == True
