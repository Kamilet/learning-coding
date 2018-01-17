'''求合并后的集合'''

def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    numbers = []
    for pairs in intervals:
        for number in range(pairs[0],pairs[1]+1):
            numbers.append(number)
    numbers = sorted(set(numbers))
    new_intervals = []
    try:
        begin = numbers[0]
    except IndexError:
        return []
    for i in range(1,len(numbers)):
        if numbers[i] - numbers[i-1] > 1:
            new_intervals.append((begin, numbers[i-1]))
            begin = numbers[i]
    new_intervals.append((begin, numbers[-1]))
    print(new_intervals)
    return new_intervals

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')
