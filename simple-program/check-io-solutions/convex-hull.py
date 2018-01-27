'''
给一组点坐标xy
围成最大的凸多边形
返回点的输入顺序，从左边最下开始，顺时针
'''


def checkio(points):
    points_set = {}
    
    # save the queue
    for p in range(len(points)):
        points_set[tuple(points[p])] = p
    # print(points_set)

    # re-range the list 错误
    '''
    points = sorted(points, key = lambda x:(x[0], x[1]))
    return_list = []
    for i in points:
        return_list.append(points_set[tuple(i)])
    print(return_list)
    '''

    # delete
    around = []
    for i in range(len(points)):
        for k in range(len(points)):
            if i == k or (points[k] in around and points[i] in around):
                continue
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[k][0], points[k][1]
            if (x1-x2):
                # print('method1')
                rate = (y1-y2)/(x1-x2)
                plus = y1 - x1 * rate
                _points = points[:]
                _points.remove(points[i])
                _points.remove(points[k])
                check = x = 0
                while not check:
                    check = _points[x][0] * rate + plus - _points[x][1]
                    x += 1
                flag = True
                for p in _points:
                    if (p[0] * rate + plus - p[1]) * check < 0:
                        flag = False
                        break
            else:
                # print('method2')
                _points = points[:]
                _points.remove(points[i])
                _points.remove(points[k])
                check = _points[0][0] - x1
                flag = True
                for p in _points[1:]:
                    if (p[0] - x1) * check < 0:
                        flag = False
                        break
            if flag:
                around.append(tuple(points[i]))
                around.append(tuple(points[k]))
                break
    around = list(set(around))
    # print(around)

    # sort
    left_b = sorted(around, key = lambda x:(x[0], x[1])) # 左边最下
    top_l = sorted(around, key = lambda x:(x[1], -x[0]), reverse=True) # 上端最左
    right_t = sorted(around, key = lambda x:(x[0], x[1]), reverse=True) # 右端最上
    bottom_r = sorted(around, key = lambda x:(x[1], -x[0])) # 下端最右
    left_b = left_b[:left_b.index(top_l[0])]
    top_l = top_l[:top_l.index(right_t[0])]
    right_t = right_t[:right_t.index(bottom_r[0])]
    bottom_r = bottom_r[:bottom_r.index(left_b[0])]
    if len(left_b):
        left_b = [left_b[0]] + [x for x in left_b[1:] if x[0]>=left_b[0][0] and x[1]>left_b[0][1]]
    if len(top_l):
        top_l = [top_l[0]] + [x for x in top_l[1:] if x[0]>top_l[0][0] and x[1]<=top_l[0][1]]
    if len(right_t):
        right_t = [right_t[0]] + [x for x in right_t[1:] if x[0]<=right_t[0][0] and x[1]<right_t[0][1]]
    if len(bottom_r):
        bottom_r = [bottom_r[0]] + [x for x in bottom_r[1:] if x[0]<bottom_r[0][0] and x[1]>=bottom_r[0][1]]
    # print(left_b,'\n',top_l,'\n',right_t,'\n',bottom_r)

    # return
    result = []
    for i in left_b:
        result.append(points_set[i])
    for i in top_l:
        result.append(points_set[i])
    for i in right_t:
        result.append(points_set[i])
    for i in bottom_r:
        result.append(points_set[i])
    # print(result)
    return result




checkio([[1,1],[1,3],[1,4],[5,1],[5,5]])
checkio([[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]) == [4, 5, 6, 0, 1, 2, 3]
checkio([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]) == [1, 0, 6, 3, 5, 2]



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
    assert checkio([[7,6],[6,5],[3,7],[3,6],[5,3],[6,2],[3,2],[2,4],[1,4]]) == [8,2,0,5,6]



'''大神解法

# migrated from python 2.7

def checkio(d):

    h, i = sorted(d) + sorted(d)[::-1], 1

    while i < len(h):

        (a,A), (b,B), (c,C) = (h*2)[i-1:i+2]

        if (b,B) == (c,C) or (c-a)*(B-A) < (b-a)*(C-A):

            h.pop(i)

            i -= i > 1

        else:

            i += 1

    return list(map(d.index, h))
'''
