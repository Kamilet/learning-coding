def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    _dict = {}
    for i in data:
        try:
            _dict[i] = _dict[i] + 1
        except:
            _dict[i] = 1
    return sorted(_dict.items(), key=lambda x:x[1])[-1][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')


'''


def most_frequent(data):

    result = {element: 0 for element in set(data)}

    for element in data:

        if element in result:

            result[element] += 1

    return max(result, key=result.get)

'''

'''

def most_frequent(data):

    

    from collections import Counter

    n = Counter(data)

    ans = n.most_common()[0]

    return ans[0]


'''