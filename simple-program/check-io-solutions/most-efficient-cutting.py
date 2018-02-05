'''
n个6000切分成几段
问浪费了多少
'''

# 未解决


def most_efficient_cutting(pieces):
    wasted = 0
    pieces = sorted(pieces)
    while len(pieces):
        long_log = 6000
        long_log -= pieces.pop()
        pieces_copy = pieces[:]
        for i in pieces_copy:
            if i <= long_log:
                long_log -= i
                pieces.remove(i)
        wasted += long_log
    print(wasted)
    return wasted


most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1300]) == 100
most_efficient_cutting([4000, 4000, 4000]) == 6000
if __name__ == '__main__':
    assert(most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1300]) == 100)
    assert (most_efficient_cutting(
        [4000, 4000, 4000]) == 6000), "wasted: 3x2000"
    assert(most_efficient_cutting([1]) == 5999), "5999"
    assert(most_efficient_cutting([3001, 3001]) == 5998), "2x2999"
    assert(most_efficient_cutting(
        [3000, 2200, 1900, 1800, 1600, 1300]) == 200), "2x5900"
    assert(most_efficient_cutting([3000]) == 3000)
    assert(most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1400]) == 0)
    most_efficient_cutting([1950, 1850, 1750, 1650, 1350, 1250, 1150, 1050])

    print('"Run" is good. How is "Check"?')
