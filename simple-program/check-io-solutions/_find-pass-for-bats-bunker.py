'''
在一个未知的矩阵里，有方格A和方格B。
在方格A和方格B中间划线，线经过了哪些方格？
返回这些方格，用list嵌套tuple来返回。
烦
'''
A = (1,0)
B = (4,0)

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


print(passedby(A,B))
