'''将给定的木头（长度length）分割成若干三角数，返回。
段数尽可能多。
若不能完成任务，返回
长度小于1000'''

def gen_triangular_number(limit):
    numbers = [0]
    height = 1
    while numbers[-1] <= limit:
        numbers.append(numbers[-1]+height)
        height+=1
    return numbers[1:]


def checkio(length):
    triangular_numbers = gen_triangular_number(length)[:-1]
    flag = False
    for begin in range(len(triangular_numbers)):
        temp_length = 0
        for begin_from_begin in range(begin, len(triangular_numbers)):
            temp_length += triangular_numbers[begin_from_begin]
            if temp_length == length:
                flag = True
                break
        if flag: break
    if flag:
        sticks = []
        for i in range(begin, begin_from_begin+1):
            sticks.append(triangular_numbers[i])
        # print(sticks)
        return sticks
    else:
        return []

assert checkio(64) == [15, 21, 28]
assert checkio(371) == [36, 45, 55, 66, 78, 91]
assert checkio(225) == [105, 120]
assert checkio(882) == []