def flatten(dictionary):
    # Solved, but I think oglop's solution 10 times better than mine...
    # https://py.checkio.org/user/oglop/
    # his solution below:
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        # (path, current)
        for k, v in current.items():
            if v == {}:
                v = ""
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result



if __name__ == '__main__':

    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"

    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')


'''大神
# 1oglop1
def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        # (path, current)
        for k, v in current.items():
            if v == {}:
                v = ""
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result
    '''


'''大神2


def flatten(D, path=[]):

    if not D: D = ""

    if isinstance(D, dict):

        res = {}

        for key, val in D.items(): res.update(flatten(val, path + [key]))

        return res

    if isinstance(D, str): return {"/".join(path): D}

'''
'''my问题代码
    flattenDictionary = {}
    for key_1 in dictionary:
        _tempkey = key_1
        _route = key_1
        digdict = dictionary
        dictdeep = dictionary
        while type(digdict[_tempkey]) is dict:
            dictdeep = digdict
            if len(digdict[_tempkey]) != 0:
                if _route != _tempkey:
                    _route = '/'.join([_route, _tempkey])
                digdict = digdict[_tempkey]
                _tempkey = list(digdict)[0]
            else:
                break
        for d in dictdeep:
            if not len(dictdeep[d]) and len(dictdeep) == 1:
                flattenDictionary[_route] = ''
                continue
            if type(dictdeep[d]) is dict:
                for i in dictdeep[d]:
                    if not len(dictdeep[d][i]):
                        flattenDictionary['/'.join([_route,i])] = ''
                    elif type(dictdeep[d][i]) is not dict:
                        flattenDictionary['/'.join([_route,i])] = dictdeep[d][i]
            else:
                flattenDictionary[_route] = dictdeep[d]
    print('theresult:\n',flattenDictionary)
    return flattenDictionary
    '''