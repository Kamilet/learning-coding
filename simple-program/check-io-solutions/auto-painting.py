'''
不好描述的涂色问题。
每个物体需要两次涂漆。
给出checkio(K,N)
有N个物体，机器每次只能画K个物体的1面。
把物体按照0-N-1编号
求每一步画了哪几个物体。
'''

def checkio(capacity, quantity):
    unpainted_faces = []
    for i in range(quantity):
        unpainted_faces.append(i)
    unpainted_faces = unpainted_faces[:]+unpainted_faces[:]
    paint_every_step = []
    while unpainted_faces:
        paint_this_step = [str(unpainted_faces[0])]
        for i in range(1,len(unpainted_faces)):
            if len(paint_this_step) == capacity or len(paint_this_step) == quantity:
                break
            if unpainted_faces[i] != unpainted_faces[i-1]:
                paint_this_step.append(str(unpainted_faces[i]))
        paint_every_step.append(''.join(paint_this_step))
        for items in paint_this_step:
            unpainted_faces.remove(int(items))

    return ','.join(paint_every_step)




checkio(2, 3)  # "01,12,02"
checkio(6, 3)  # "012,012"
checkio(3, 6)  # "012,012,345,345"
checkio(1, 4)  # "0,0,1,1,2,2,3,3"
checkio(2, 5)  # "01,01,23,42,34"