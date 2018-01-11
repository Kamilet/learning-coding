def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    sets = []
    data = sorted(list(data))
    if len(data) == 0:
        return sets
    if len(data) == 1:
        if type(data[0]) is int:
            return [(data[0], data[0])]

    _begin = data[0]
    for index in range(1,len(data)):
        if data[index] != data[index-1]+1:
            sets.append((_begin,data[index-1]))
            _begin = data[index]
        if index == len(data)-1:
            sets.append((_begin,data[index]))
    return sets

#create_intervals({1, 2, 3, 6, 7, 8, 4, 5})
print(create_intervals([1]))
assert create_intervals([1]) == [(1, 1)]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    #assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
