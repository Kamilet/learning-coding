'''
给定一个字符串（可以多行）
给定一个list
鉴定list里每个item出现的次数
list里的item都是小写
鉴定不分大小写
'''
import re

def popular_words(text, words):
    text = (text.lower()).split('\n| |,|.')
    print(text)

    return None


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
