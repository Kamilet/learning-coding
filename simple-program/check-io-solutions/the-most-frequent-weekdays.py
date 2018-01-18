'''
计算某年内最多的是星期几
'''

# dict
week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
        6: 'Saturday', 7: 'Sunday'}


# a part of my solution for days-diff
def days_number(date: str):
    '''give a number like 20000101, return the count number:
    0000-00-01 means 1, 0000-00-02 means 2...'''
    dict_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                  8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    _year_2_day = (int(date[0:4])-1)*365 + (int(date[0:4])-1)//4 - \
        (int(date[0:4])-1)//100 + (int(date[0:4])-1)//400

    _mon = int(date[4:6])
    _month_2_day = 0
    while _mon > 1:
        _month_2_day += dict_month[_mon-1]
        _mon -= 1

    if int(date[0:4]) % 4 == 0 and int(date[0:4]) % 100 != 0 and int(date[4:6]) > 2:
        _month_2_day += 1

    _day = int(date[6:])

    return _year_2_day + _month_2_day + _day


# new function
def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    begin = days_number(''.join([str(year).zfill(4), '0101']))
    end = days_number(''.join([str(year).zfill(4), '1231']))
    begin %= 7
    end %= 7
    if not end:
        end = 7
    if not begin:
        begin = 7
    if begin == end:
        return [week[begin]]
    else:
        return [week[min(begin, end)], week[max(begin, end)]]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
    assert most_frequent_days(1216) == ["Friday", "Saturday"]
