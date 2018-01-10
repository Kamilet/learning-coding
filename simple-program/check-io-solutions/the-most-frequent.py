'''
 DahliaSR [Follow] 2 hours ago The Counters Most Common 0

Never use blank excepts, also make sure you are only catching specific exceptions instead of any exception:

except KeyError:
    _dict[i] = 1

In this case it would be better to avoid that a key is not present in _dict, by using dict.fromkeys():

# init a dict where each string from data is present is a key, with value = 0
_dict = dict.fromkeys(data, 0)

max() instead of sorted() would have been the better choice.

return max(_dict.items, key=lambda x: x[1])[0]


'''

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