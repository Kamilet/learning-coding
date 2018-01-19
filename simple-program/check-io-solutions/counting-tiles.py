'''
圆里切方的问题。
给一个半径N，以半径画圆，切出最大的正方形，面积为solid。
而被圆圈到却不能形成正方形的面积为partial。
两个面积都以方格为单位，即几个方格。
'''
def checkio(radiu):
    one_quarter_block_lenth = int(radiu) + (not (int(radiu) == radiu))
    solid_one_quarter = 0
    partial_one_quarter = 0
    for x in range(one_quarter_block_lenth):
        for y in range(one_quarter_block_lenth):
            p_far = distance(x+1,y+1)
            p_close = distance(x,y)
            if p_far <= radiu:
                solid_one_quarter += 1
            elif p_close < radiu:
                partial_one_quarter += 1
    return [solid_one_quarter*4, partial_one_quarter*4]


def distance(x,y):
    return (x**2 + y**2)**0.5


checkio(2) # [4, 12]
checkio(3) # [16, 20]
checkio(2.1) # [4, 20]
checkio(2.5) # [12, 20]