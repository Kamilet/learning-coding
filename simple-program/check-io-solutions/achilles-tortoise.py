'''
追击问题
输入checkio(v_fast,v_slow,advantage)
v_fast和v_slow代表两人速度
advantage代表慢的人领先的时间
求追击时间
'''


def chase(v_fast, v_slow ,advantage):
    chase_time = advantage * v_fast / (v_fast - v_slow)
    # print(round(chase_time,8))
    return round(chase_time,8)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"
