'''判断天数差距'''
# 不使用time库

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    date1 = ''.join([str(date1[0]).zfill(4), str(date1[1]).zfill(2), str(date1[2]).zfill(2)])
    date2 = ''.join([str(date2[0]).zfill(4), str(date2[1]).zfill(2), str(date2[2]).zfill(2)])
    return abs(days_number(date1) - days_number(date2))

def days_number(date:str):
    '''give a number like 20000101, return the count number:
    0000-00-01 means 1, 0000-00-02 means 2...'''
    dict_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,
                  8:31,9:30,10:31,11:30,12:31}
    _year_2_day = (int(date[0:4])-1)*365 + (int(date[0:4])-1)//4 - (int(date[0:4])-1)//100 + (int(date[0:4])-1)//400

    _mon = int(date[4:6])
    _month_2_day = 0
    while _mon > 1:
        _month_2_day += dict_month[_mon-1]
        _mon -= 1

    if int(date[0:4])%4 == 0 and int(date[0:4])%100 != 0 and int(date[4:6]) > 2:
        _month_2_day += 1

    _day = int(date[6:])

    return _year_2_day + _month_2_day + _day

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print(days_diff((1,1,1), (9999,12,31)))
    print(days_number('00010301'))
    print(days_number('99991231'))
    print(days_number('20091001'))  #733681
    print(days_diff((7410,4,9), (9884,3,16)))
    assert days_diff((1,1,1), (9999,12,31)) == 3652058
    assert days_diff((1970,1,1), (2000,1,1)) == 10957
    assert days_diff((7410,4,9), (9884,3,16)) == 903587
