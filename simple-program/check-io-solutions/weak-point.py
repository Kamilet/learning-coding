'''
找出弱点
'''


def weak_point(matrix):
    check_row = [0]*len(matrix)
    check_colume = [0]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            check_row[i] += matrix[i][j]
            check_colume[j] += matrix[i][j]
    row_min = min(check_row)
    colume_min = min(check_colume)
    weak_points = []
    for i in range(len(check_row)):
        for j in range(len(check_colume)):
            if check_row[i] == row_min and check_colume[j] == colume_min:
                weak_points.append([matrix[i][j], i, j])
    return sorted(weak_points, key=lambda x: x[0])[0][1:]


weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [3, 3]

weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [1, 2]
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)
                      ), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
