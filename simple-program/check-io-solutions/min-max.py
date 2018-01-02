'''
尝试自己写出max或min的教程，理解内建函数
'''

# too hard for me.. :cry:
# I'll try anyway
def my_min(*args, **kwargs):
    key = kwargs.get("key", None)
    return sort_big_small(args, key, True)


def my_max(*args, **kwargs):
    key = kwargs.get("key", None)
    return sort_big_small(args, key, False)


def sort_big_small(args, key, switch = False):
    '''set False to get the smallest one'''
    lists = []
    # special when len = 1
    # if isalpha, return the biggest alpht in ASCII
    # if number, return the number it self # as the original founction max()
    # if list, translate it
    if 'lambda' in str(key) and len(args) == 1:
        # here i get a way to solve the lambda case after trying...
        _count = len(args[0])
        for i in range(0, _count):
            lists.append(key(args[0][i]))
        return args[0][bubble_max(lists, switch)]
    if len(args) == 1:
        if type(args[0]) == list or type(args[0]) == tuple:
            return args[0][bubble_max(args[0], switch)]
        elif str(args[0]).isalpha():
            _count = len(args[0])
            for i in range(0, _count):
                lists.append(args[0][i])
            return lists[bubble_max(lists, switch)]
        else:
            return args[0]

    # if len > 1, check key first
    # 2018-01-02 dammmm I don't know how to deal with it :heart_break:
    if key != None:
        for item in args:
            # doesn't work for lambda at all
            # in this case:
            # print(my_min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
            # then process here...
            # print(lists)
            # just get a [1, 2]
            # then i added another branch, hoping that will work
            lists.append(key(item))
    else:
        lists = list(args)
    # get just position and return from origin set
    # for expansion
    # --- tested when numbers only :smile:
    # print(my_max(1,10,1,1,2,1,451,1,1,111,2221,1,1,1,1,9,1))
    # print(my_min(1,3,13,1,2,1,451,1,11,0,1,1,1,1,1,9,1))
    # --- tested when alpha only :smile:
    # print(my_max('A','C','B'))
    # --- tested when one string only :smile:
    # print(my_max(123))
    # print(my_max(aBc))
    # --- tested when a float inside with the key: int :smile:
    # print(my_max(444,631,1256.3,key = int))
    # --- tested when its only list :smile:
    # print(my_max([1, 2, 0, 3, 4]))
    # --- tested when a lambda function used
    # print(my_min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
    # [filed check] with: min((9,))
    # solved
    # [filed check] with: max(range(6))
    return args[bubble_max(lists, switch)]


def bubble_max(lists, switch = False):
    '''Bubble Sort. Standard.
    I choice it because wanted to get the position of the max one or the min one.
    I thought return the position could be better when expand it... may be not.
    Set to False to get the position of smallest one.'''
    _count = len(lists)
    if switch:
        _position_min = 0
        k = 0
        for i in range(0, _count):
            if i < k:
                continue
            for k in range(i+1, _count):
                if lists[i] > lists[k]:
                    _position_min = k
                    i = k
                    break
        return _position_min
    else:
        _position_max = 0
        k = 0
        for i in range(0, _count):
           if i < k:
               continue
           for k in range(i+1, _count):
               if lists[i] < lists[k]:
                   _position_max = k
                   i = k
                   break
        return _position_max
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert my_max(3, 2) == 3, "Simple case max"
    assert my_min(3, 2) == 2, "Simple case min"
    assert my_max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert my_min("hello") == "e", "From string"
    assert my_max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert my_min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''
print(range(6))
print(max(range(6)))