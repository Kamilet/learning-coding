'''
刷墙
给一个数字和一个列表，列表是刷第几格到第几格墙
数字是需求的长度
返回有几个符合这个长度的刷过的墙
不重合计算

理解错误，返回达到长度时刷到第几步……
'''

# 未提交，未解锁

def checkio(request, solution=[]):
    solution.append([0,0])
    painted_walls = []
    wall_requested = -1
    for paint_start, paint_end in solution:
        painted_walls = sorted(painted_walls, key = lambda x:x[0])
        # sort
        if len(painted_walls)>1:
            for i in range(1,len(painted_walls)):
                if painted_walls[i-1][1]>=painted_walls[i][0]:
                    painted_walls[i] = [painted_walls[i-1][0], painted_walls[i][1]]
                    painted_walls[i-1] = [0,0]
        while [0,0] in painted_walls:
            painted_walls.remove([0,0])
        # sortend
        # check
        flag = True
        wallnow = 0
        for painted_start, painted_end in painted_walls:
            wallnow += (painted_end - painted_start + 1)
            if wallnow >= request:
                wall_requested = solution.index([paint_start, paint_end])
                flag = False
        if not flag:
            break
        # checkend
        # print('before',painted_walls)
        # print('insert',paint_start,paint_end)
        s,e = paint_start, paint_end
        for painted_start, painted_end in painted_walls:
            if (s <= painted_end and s >= painted_start) or\
               (e <= painted_end and e >= painted_start):
               painted_walls.remove([painted_start, painted_end])
               s, e = min(s,e,painted_start,painted_end),\
                      max(s,e,painted_start,painted_end)
               painted_walls.append([s, e])
               flag = False
        if flag:
            painted_walls.append([paint_start, paint_end])
        # print('then',painted_walls)
    # print(wall_requested)
    # print(painted_walls)
    return wall_requested


checkio(5, [[1,5], [11,15], [2,14], [21,25]]) == 1 # The first operation will paint 5 meter long.
checkio(6, [[1,5], [11,15], [2,14], [21,25]]) == 2 # The second operation will paint 5 meter long. The sum is 10.
checkio(11, [[1,5], [11,15], [2,14], [21,25]]) == 3 # After the third operation, the range 1-15 will be painted.
checkio(16, [[1,5], [11,15], [2,14], [21,25]]) == 4 # Note the overlapped range must be counted only once.
checkio(21, [[1,5], [11,15], [2,14], [21,25]]) == -1 # There are no ways to paint for 21 meters from this list.
checkio(1000000011,[[1,1000000000],[11,1000000010]]) == -1 # One of the huge test cases.