'''
输入：
我的坐标：
MN
M in [A, B, C...]
N in [1, 2, 3...]
六边形坐标

我的方向：
direction in ('N', 'NE', 'SE', 'S', 'SW', 'NW').

敌人坐标：
MN
M in [A, B, C...]
N in [1, 2, 3...]

输出敌人所在方位
输出和敌人的距离

比如
find_enemy('B2', 'S', 'B4') == ['F', 2]

#未解决
'''
# MT_DIRECTION = {'N':(0,0),'S':(-1,1),'NE':(-1,1),'SE':(1,1),'NW':(-1,-1),'SW':(-1,1)}


def find_enemy(my_position, my_direction, enemy_position):
    # distance = 1
    # direction = 'F' # {'F':'Front', 'B':'Back', 'L':'Left', 'R':'Right'}
    # calculate distance
    a = ord(enemy_position[0]) - ord(my_position[0])
    b = int(enemy_position[1]) - int(my_position[1])
    distance = max(abs(a),abs(b))
    # print(distance)
    '''
    a, b = max(a,b), min(a,b)
    if not b:
        distance = a
    else:
        sqrt_3 = 1.7320508075688772935274463415059
        distance = ((a + b * 0.5) ** 2 + (b * 0.5 * sqrt_3)) ** 0,5
    '''
    # calculate direction
    # turn to front
    
    return 0






# print(find_enemy('B2', 'S', 'B4')) #['F', 2]
if __name__ == '__main__':
    assert find_enemy('G5', 'N', 'G4') == 0#['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == 0#['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == 0#['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == 0#['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == 0#['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == 0#['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == 0#['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == 0#['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == 0#['L', 12], "true left"
    #print("You are good to go!")