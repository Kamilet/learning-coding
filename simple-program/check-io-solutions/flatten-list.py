'''
将多层数组拆开
代码少于160字符
'''

# 未提交，没解锁

def flat_list(mess_list, flag=True):
    while flag:
        flag = False
        for i in mess_list:
            if type(i) is list:
                mess_list += i
                mess_list.remove(i)
                flag = True
                break
    return mess_list

flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]