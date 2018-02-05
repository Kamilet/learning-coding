'''
https://py.checkio.org/mission/all-the-same/
'''


def all_the_same(args):
    if len(args):
        args = sorted(args, key=lambda x: str(x))
        return args[0] == args[-1]
    else:
        return True

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
