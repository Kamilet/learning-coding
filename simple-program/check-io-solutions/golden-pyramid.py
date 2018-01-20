'''
金字塔路线
'''

def count_gold(pyramid):
    '''最大的下金字塔路线'''
    hight = len(pyramid)
    row_replace = list(pyramid[-1])
    row_now = [0]*hight
    for i in range(hight-2, -1, -1):
        for k in range(len(pyramid[i])):
            row_now[k] = pyramid[i][k] + max(row_replace[k], row_replace[k+1])
        row_replace = row_now[:]
    return row_replace[0]


assert count_gold((
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3))) == 23

assert count_gold((
    (1,),
    (2, 1),
    (1, 2, 1),
    (1, 2, 1, 1),
    (1, 2, 1, 1, 1),
    (1, 2, 1, 1, 1, 1),
    (1, 2, 1, 1, 1, 1, 9))) == 15

assert count_gold((
    (9,),
    (2, 2),
    (3, 3, 3),
    (4, 4, 4, 4))) == 18

'''    gold = pyramid[0][0]
    k = 0
    p_o = pyramid[0][0]
    for i in range(1,len(pyramid)):
        p_one = pyramid[i][k]
        p_two = pyramid[i][k+1]
        if p_o == p_two:
            gold += p_two
            k += 1
            print(p_two,k)
        elif p_o == p_one:
            gold += p_one
            print(p_two,k,'er')
        elif p_one > p_two:
            gold += p_one
            p_o = p_one
            print(p_one,k)
        else:
            gold += p_two
            k += 1
            p_o = p_two
            print(p_two,k,'si')
    print(gold)
    '''
