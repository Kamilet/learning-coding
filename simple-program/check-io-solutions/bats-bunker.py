
def checkio(bunker):
    # set
    waypoints = []
    blocks = []
    for i in range(len(bunker)):
        for k in range(len(bunker[0])):
            if bunker[i][k] == 'B':
                waypoints.append((i, k))
            elif bunker[i][k] == 'W':
                blocks.append((i, k))
            elif bunker[i][k] == 'A':
                waypoints.append((i, k))
                endpoint = (i, k)
    startpoint = waypoints[0][:]
    # print(blocks)
    # blocks = blocks + waypoints
    # try any routes for any bats
    # print(access([1,0],[2,1],blocks))
    # input()
    batpath = {}
    # print('bats',waypoints)
    for i in range(len(waypoints) - 1):
        for k in range(i + 1, len(waypoints)):
            if access(waypoints[i], waypoints[k], blocks):
                batpath.setdefault(waypoints[i], []).append(waypoints[k])
                batpath.setdefault(waypoints[k], []).append(waypoints[i])
    # print('path',batpath)
    # learned from jingyuan
    active = (0, 0)
    open = [active]
    closed = []
    status = dict()
    status[active] = (0, distance([active, endpoint]), None)
    while active != endpoint:
        open.remove(active)
        closed.append(active)
        nextroute = batpath[active]
        for n in nextroute:
            if n in closed:
                continue
            if n not in open:
                open.append(n)
                status[n] = [status[active][0] + distance([n, active]), distance([n, endpoint]), active]
            else:
                disg = status[active][0] + distance([n, active])
                if status[n][0] > disg:
                    status[n][0] = disg
                    status[n][2] = active
        f = 10000
        for i in open:
            if status[i][0] + status[i][1] < f:
                f = status[i][0] + status[i][1]
                active = i
    # now = active
    # while status[now][2]:
    #    now = status[now][2]
    # print(status[active][0] + status[active][1])
    return status[active][0] + status[active][1]


def access(point_1, point_2, blocks):
    # return True if access
    # 准备重写，单独函数：在两个格子中间划线，经过哪几个格子
    # 检验这些格子，然后看有没有blocks
    
    # 检查结束，返回经过的格子passedby
    for point in passedby(point_1,point_2):
        if point in blocks:
            return False
    return True


def distance(points):
    # return distance from begin to end
    from math import sqrt
    distance = 0
    for i in range(len(points)-1):
        distance += sqrt((points[i][0] - points[i+1][0])**2 +
                         (points[i][1] - points[i+1][1])**2)
    return distance


def passedby(pa, pb):
    ax, ay = pa
    bx, by = pb
    dx = ax - bx
    dy = ay - by
    passed = []
    if dx == 0:
        for y in range(min(ay,by),max(ay,by)):
            passed.append((ax,y))
    elif dy == 0:
        for x in range(min(ax,bx),max(ax,bx)):
            passed.append((x,ay)) 
    else:
        # list the blocks that need to check:
        _check = []
        for i in range(min(ax,bx), max(ax,bx)+1):
            for k in range(min(ay,by), max(ay,by)+1):
                _check.append((i,k))
        passed = _check[:]
        # print(passed)
        # make a fomula with (x+0.5,y+0.5)
        rate = (ax-bx) / (ay-by)
        plus = bx+0.5 - (by+0.5) * rate
        # print('y=({})x+({})'.format(rate,plus))
        for item in _check:
            if abs((item[1]+0.5)*rate-(item[0]+0.5)+plus)/((rate**2+1)**0.5) > 0.70710678118654752440084436210485:
                # print('item:',item[1]+0.5,item[0]+0.5)
                # print('online:',item[1]+0.5,(item[1]+0.5)*rate+plus)
                passed.remove(item)
    # print(passed)
    return passed


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"

    '''
        _xl = abs(point_1[1] - point_2[1])
    _yl = abs(point_1[0] - point_2[0])
    _x = min(point_1[1], point_2[1])
    _y = min(point_1[0], point_2[0])
    if not _yl and _xl:
        for x in range(1, _xl+1):
            if (_x + x, _y) in blocks:
                return False
    if not _xl and _yl:
        for y in range(1, _yl):
            if (_x, _y + y) in blocks:
                return False
    if _xl and _yl:
        if _xl == _yl:
            if point_1[0] < point_2[0] and point_1[1] < point_2[1]:
                for i in range(1, _xl):
                    if (_x + i, _y + i) in blocks:
                        return False
            # 修改，关于右上左下
        else:
            if _xl > _yl:
                for x in range(1, _xl+1):
                    for y in range(0, _yl):
                        print(_x+x,_y+y)
                        if (_x + x, _y + y) in blocks:
                            return False
            else:
                for y in range(0, _yl):
                    for x in range(1, _xl+1):
                        if (_x + x, _y + y) in blocks:
                            return False
    return True
    '''
    '''
    def access(point_1, point_2, blocks):
    # return True if access
    # 准备重写，单独函数：在两个格子中间划线，经过哪几个格子
    # 检验这些格子，然后看有没有blocks
    p1x = point_1[0]
    p1y = point_1[1]
    p2x = point_2[0]
    p2y = point_2[1]
    if p1x == p2x:
        py = min(p1y,p2y)
        for i in range(abs(p1y-p2y)+1):
            if (p1x, py+i) in blocks:
                return False
    elif p1y == p2y:
        px = min(p1x,p2x)
        for i in range(abs(p1x-p2x)+1):
            if (px+i, p1y) in blocks:
                return False
    elif (p1x>p2x and p1y>p2y) or (p2x>p1x and p2y>p1y):
        px = min(p1x,p2x)
        py = min(p1y,p2y)
        for i in range(min(abs(p1x-p2x),abs(p1y-p2y))+1):
            # print(px+i,py+i,'checked',end='   ')
            if abs(p1y-p2y)>abs(p1x-p2x):
                if (px+i,py+i) in blocks or (px+i,py+i+1) in blocks or (px+i,py+i-1) in blocks:
                    return False
            else:
                if (px+i,py+i) in blocks or (px+i-1,py+i) in blocks or (px+i+1,py+i) in blocks:
                    return False
        px = max(p1x,p2x)
        py = max(p1y,p2y)
        for i in range(min(abs(p1x-p2x),abs(p1y-p2y))+1):
            if abs(p1y-p2y)>abs(p1x-p2x):
                if (px-i,py-i) in blocks or (px-i,py-i+1) in blocks or (px-i,py-i-1) in blocks:
                    return False
            else:
                if (px-i,py-i) in blocks or (px-i+1,py-i) in blocks or (px-i+1,py-i) in blocks:
                    return False
    else:
        px = min(p1x,p2x)
        py = max(p1y,p2y)
        # print('checking',px,py,'and 左下')
        for i in range(min(abs(p1x-p2x),abs(p1y-p2y))+1):
            # print(px+i,py-i,'checked',end='   ')
            if abs(p1y-p2y)>abs(p1x-p2x):
                if (px+i,py-i) in blocks or (px+i,py-i+1) in blocks or (px+i,py-i-1) in blocks:
                    return False
            else:
                if (px+i,py-i) in blocks or (px+i+1,py-i) in blocks or (px+i-1,py-i) in blocks:
                    return False
        px = max(p1x,p2x)
        py = min(p1y,p2y)
        for i in range(min(abs(p1x-p2x),abs(p1y-p2y))+1):
            if abs(p1y-p2y)>abs(p1x-p2x):
                if (px-i,py+i) in blocks or (px-i,py+i+1) in blocks or (px-i,py+i-1) in blocks:
                    return False
            else:
                if (px-i,py+i) in blocks or (px-i+1,py+i) in blocks or (px-i+1,py+i) in blocks:
                    return False
    return True
'''