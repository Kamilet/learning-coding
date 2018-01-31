'''
有quantity个骰子，每个face面，求得到number和的概率
骰子的face从1-face
'''
# 未解决，办事。。

def probability(quantity, face, number):
    posibility = 0
    if number >= quantity and number <= face * quantity:
        maxnum = quantity * face * 0.5 + 1
        posibility = (maxnum - abs(maxnum - number)-1) / face ** quantity
    print(posibility)
    return posibility


probability(2, 6, 3) == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
probability(2, 6, 4) == 0.0833
probability(2, 6, 7) == 0.1667
probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
probability(2, 3, 7) == 0       # The maximum you can roll on 2 three-sided dice is 6
probability(3, 6, 7) == 0.0694
probability(10, 10, 50) == 0.0375