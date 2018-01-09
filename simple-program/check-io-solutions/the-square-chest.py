'''
一个4x4的点阵，如果输入[[1, 2], [3, 4], [1, 5], [2, 6], [5,6]]是这样的：
——————————————
1 ——2   3 - 4
|   |
5 ——6   7   8

9   10  11  12

13  14  15  16 
———————————————
给出类似的数组，数出里面的正方形
'''

def checkio(lines_list):
    """Return the quantity of squares"""
    row = [[0]*3,[0]*3,[0]*3,[0]*3]
    colume = [[0]*4,[0]*4,[0]*4]
    square = 0
    # save line in matrix
    for i in lines_list:
        if i[0]-i[1] in [-1,1]:
            row[int((i[0]-1)/4)][min(i[0],i[1])%4-1] = 1
        else:
            colume[int(((min(i[0],i[1])-1)/4))][min(i[0],i[1])%4-1] = 1

    for r in [0, 1, 2]:
        # r is the start point of row
        for c in [0, 1, 2]:
            # c is the start point of colume
            for line in range(1, 4-max(r,c)):
                # line is the length of square
                check = 0
                print(line)
                for i in range(0, line):
                    check = row[r][c+i] + colume[r+i][c] + row[r+line][c+i] + colume[r+i][c+line] + check
                if check == line * 4:
                    square += 1
    return square


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"