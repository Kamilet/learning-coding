'''
倒水问题
0代表水池
1代表试管1
2代表试管2
求测量出x大小的水的每一步骤
'''


def checkio(cup_a, cup_b, need):

    # sort
    _ori = '0'
    if cup_a > cup_b:
        _big = '1'
        _sma = '2'
        cup_a, cup_b = cup_b, cup_a
    else:
        _big = '2'
        _sma = '1'

    # handle
    # 大优先思路：ab必有1空或1满
    # a永不入b
    # 水源永不填满a
    # b永远不会倒掉
    cup_a_water = 0
    cup_b_water = cup_b
    steps_b = [_ori+_big]
    while cup_a_water != need and cup_b_water != need:
        if not cup_b_water:
            # b空必满
            cup_b_water = cup_b
            steps_b.append(_ori+_big)
        elif not cup_a_water:
            # a空必b入
            cup_a_water = min(cup_a, cup_b_water)
            cup_b_water = max(cup_b_water - cup_a, 0)
            steps_b.append(_big+_sma)
        elif cup_b_water == cup_b:
            # b满必入a
            cup_b_water -= (cup_a - cup_a_water)
            cup_a_water = cup_a
            steps_b.append(_big+_sma)
        elif cup_a_water == cup_a:
            # a满必倒
            cup_a_water = 0
            steps_b.append(_sma+_ori)
        else:
            # ..
            print('error')
            break
    # 小优先思路，同上
    cup_a_water = cup_a
    cup_b_water = 0
    steps_s = [_ori+_sma]
    while cup_a_water != need and cup_b_water != need:
        if not cup_a_water:
            # a空必满
            cup_a_water = cup_a
            steps_s.append(_ori+_sma)
        elif not cup_b_water:
            # b空必a入
            cup_b_water = cup_a_water
            cup_a_water = 0
            steps_s.append(_sma+_big)
        elif cup_a_water == cup_a:
            # a满必入b
            cup_a_water = max(cup_a_water - cup_b + cup_b_water, 0)
            cup_b_water = min(cup_b, cup_b_water + cup_a)
            steps_s.append(_sma+_big)
        elif cup_b_water == cup_b:
            # b满必倒
            cup_b_water = 0
            steps_s.append(_big+_ori)
        else:
            # ..
            print('error')
            break
    if len(steps_b) > len(steps_s):
        return steps_s
    else:
        return steps_b


checkio(5, 7, 6) == ['02', '21', '10', '21',
                     '02', '21', '10', '21', '02', '21']
checkio(3, 4, 1) == ["02", "21"]
checkio(8, 5, 2)  # 02,21,02,21
checkio(2, 1, 1)
