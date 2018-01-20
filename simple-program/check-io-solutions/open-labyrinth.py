'''
走迷宫问题，输出每一步，用WNSE来输出。  
从左上到右下。0是路，1是墙。不需要去找最短的。  

### 思路
 
'''

'''
The labyrinth has no walls, but bushes surround the path on each side. 
If a players move into a bush, they lose. The labyrinth is presented as 
a matrix (a list of lists): 1 is a bush and 0 is part of the path. 
The labyrinth's size is 12 x 12 and the outer cells are also bushes. 
Players start at cell (1,1). The exit is at cell (10,10). 
You need to find a route through the labyrinth. Players can move in only fou 
directions--South (down [1,0]), North (up [-1,0]), East (right [0,1]), West (left [0, -1]). 
The route is described as a string consisting of different characters: 
"S"=South, "N"=North, "E"=East, and "W"=West.  

走迷宫问题，输出每一步，用WNSE来输出。  
从左上到右下。0是路，1是墙。不需要去找最短的。  
DIRECTION[10*(r-row)+(c-colume)]来抽取WASD。
'''

'''
未成功……
'''


DIRECTION = {10:'S',-10:'N',1:'E',-1:'W',0:''}
ROUTE = []

def checkmaze(maze_map,x=1,y=1):
    if x == len(maze_map[0])-2 and y == len(maze_map)-2:
        print('check success')
        ROUTE.append((x,y))
        return True
    if maze_map[x][y] == 0:
        ROUTE.append((x,y))
        maze_map[x][y] = 8
        if not checkmaze(maze_map,x,y+1):
            maze_map[x][y] = 0
            ROUTE.remove((x,y+1))
        elif not checkmaze(maze_map,x+1,y):
            maze_map[x][y] = 0
            ROUTE.remove((x+1,y))
        elif not checkmaze(maze_map,x,y-1):
            maze_map[x][y] = 0
            ROUTE.remove((x,y-1))
        elif not checkmaze(maze_map,x-1,y):
            maze_map[x][y] = 0
            ROUTE.remove((x-1,y))
        else:
            return False
    return True


def checkio(maze_map):
    checkmaze(maze_map)
    route = []
    m,n = 1,1
    xx = []
    yy = []
    for i in range(len(ROUTE)):
        xx.append(ROUTE[i][0])
        yy.append(ROUTE[i][1])
    for x,y in ROUTE:
        if (x == m and y in yy) or (y == n and x in xx):
            route.append((x,y))
            m,n = x,y
    print(route,'route!')


## 下面这个方法深度溢出……


'''
建立一个函数findpath(p_from)，输入起点，返回一组相邻的，可以到的点坐标。  
对每个点，调用一次findpath，从返回的结果里找下一个点。  
findpath返回了空数组的时候，掐掉。  
直到终点出现在findpath里，掐掉纪录。  

调用每个点的时候，将WNSE输入TEMP。  
掐掉纪录的时候，将TEMP输入ROUTE。  
在ROUTE里找出最小的。 

DIRECTION = {10:'S',-10:'N',1:'E',-1:'W',0:''}
ROUTE = []

def direct(frompoint, nowpoint):
    return DIRECTION[(nowpoint[0]-frompoint[0])*10+(nowpoint[1]-frompoint[1])]

def findpath(point,maze_map):
    possible_direction = []
    row, colume = point
    for r,c in [(row+1,colume), (row,colume+1), (row-1,colume), (row,colume-1)]:
        if maze_map[r][c] == 0:
            possible_direction.append((r,c))
    return possible_direction


def where_to_go(frompoint, nowpoint, endpoint, maze_map, TEMP=[]):
    TEMP.append(direct(frompoint, nowpoint))
    path = findpath(nowpoint, maze_map)
    if endpoint in path:
        TEMP.append(direct(nowpoint, endpoint))
        ROUTE.append(TEMP)
        return 0
    elif len(path) == 1:
        return 0
    else:
        for p in path:
            where_to_go(nowpoint, p, endpoint, maze_map, TEMP)


def checkio(maze_map):
    global ROUTE
    len_row = len(maze_map)
    len_column = len(maze_map[0])
    where_to_go((1,1),(1,1),(len_row-2,len_column-2),maze_map)
    print(ROUTE)
'''

a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

checkio(a)
print(a)
'''
[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 8, 0, 8, 0, 8, 0, 8, 0, 0, 8, 1], 
[1, 0, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1], 
[1, 8, 1, 0, 0, 0, 0, 0, 0, 8, 0, 1], 
[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 8, 1], 
[1, 8, 1, 0, 1, 8, 0, 0, 8, 0, 8, 1], 
[1, 0, 8, 0, 1, 1, 8, 1, 1, 1, 8, 1], 
[1, 0, 1, 8, 0, 8, 0, 1, 0, 1, 1, 1], 
[1, 0, 1, 1, 0, 1, 0, 8, 0, 8, 0, 1], 
[1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 8, 1], 
[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
'''
print(ROUTE)