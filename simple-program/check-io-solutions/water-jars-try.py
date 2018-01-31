def witch_better(cup_a, cup_b, need):
        # sort
    _ori = '0'
    if cup_a > cup_b:
        _big = '1'
        _sma = '2'
        cup_a, cup_b = cup_b, cup_a
    else:
        _big = '2'
        _sma = '1'

    cup_a_water = 0
    cup_b_water = cup_b
    steps = [_ori+_big]
    while cup_a_water != need and cup_b_water != need:
        if not cup_b_water:
            # b空必满
            cup_b_water = cup_b
            steps.append(_ori+_big)
        elif not cup_a_water:
            # a空必b入
            cup_a_water = min(cup_a, cup_b_water)
            cup_b_water = max(cup_b_water - cup_a, 0)
            steps.append(_big+_sma)
        elif cup_b_water == cup_b:
            # b满必入a
            cup_b_water -= (cup_a - cup_a_water)
            cup_a_water = cup_a
            steps.append(_big+_sma)
        elif cup_a_water == cup_a:
            # a满必倒
            cup_a_water = 0
            steps.append(_sma+_ori)
        else:
            # ..
            print('error')
    #print('大优先{}步'.format(len(steps)), steps)
    a = len(steps)
    cup_a_water = cup_a
    cup_b_water = 0
    steps = [_ori+_sma]
    while cup_a_water != need and cup_b_water != need:
        if not cup_a_water:
            # a空必满
            cup_a_water = cup_a
            steps.append(_ori+_sma)
        elif not cup_b_water:
            # b空必a入
            cup_b_water = cup_a_water
            cup_a_water = 0
            steps.append(_sma+_big)
        elif cup_a_water == cup_a:
            # a满必入b
            cup_a_water = max(cup_a_water - cup_b + cup_b_water, 0)
            cup_b_water = min(cup_b, cup_b_water + cup_a)
            steps.append(_sma+_big)
        elif cup_b_water == cup_b:
            # b满必倒
            cup_b_water = 0
            steps.append(_big+_ori)
        else:
            # ..
            print('error')
            break
    #print('小优先{}步'.format(len(steps)), steps, '\n')
    if a > len(steps):
        a = '小'
    else:
        a = '大'
    print(cup_a, cup_b, '|', need, '|', a)


witch_better(5, 7, 6)
witch_better(5, 8, 6)
witch_better(5, 9, 6)
witch_better(5, 11, 6)
witch_better(3, 4, 1)
witch_better(8, 5, 2)
witch_better(2, 5, 1)
witch_better(4, 10, 2)

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
    if (cup_a + cup_b) % 2 == need % 2:
        # 大优先思路：ab必有1空或1满
        # a永不入b
        # 水源永不填满a
        # b永远不会倒掉
        cup_a_water = 0
        cup_b_water = cup_b
        steps = [_ori+_big]
        while cup_a_water != need and cup_b_water != need:
            if not cup_b_water:
                # b空必满
                cup_b_water = cup_b
                steps.append(_ori+_big)
            elif not cup_a_water:
                # a空必b入
                cup_a_water = min(cup_a, cup_b_water)
                cup_b_water = max(cup_b_water - cup_a, 0)
                steps.append(_big+_sma)
            elif cup_b_water == cup_b:
                # b满必入a
                cup_b_water -= (cup_a - cup_a_water)
                cup_a_water = cup_a
                steps.append(_big+_sma)
            elif cup_a_water == cup_a:
                # a满必倒
                cup_a_water = 0
                steps.append(_sma+_ori)
            else:
                # ..
                print('error')
                break

    else:
        cup_a_water = cup_a
        cup_b_water = 0
        steps = [_ori+_sma]
        while cup_a_water != need and cup_b_water != need:
            if not cup_a_water:
                # a空必满
                cup_a_water = cup_a
                steps.append(_ori+_sma)
            elif not cup_b_water:
                # b空必a入
                cup_b_water = cup_a_water
                cup_a_water = 0
                steps.append(_sma+_big)
            elif cup_a_water == cup_a:
                # a满必入b
                cup_a_water = max(cup_a_water - cup_b + cup_b_water, 0)
                cup_b_water = min(cup_b, cup_b_water + cup_a)
                steps.append(_sma+_big)
            elif cup_b_water == cup_b:
                # b满必倒
                cup_b_water = 0
                steps.append(_big+_ori)
            else:
                # ..
                print('error')
                break
    print(steps)
    return steps
'''
