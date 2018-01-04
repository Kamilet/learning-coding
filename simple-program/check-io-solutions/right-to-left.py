'''One of the robots is charged with a simple task:
to join a sequence of strings into one sentence to produce
instructions on how to get around the ship.
But this robot is left-handed and has a tendency
to joke around and confuse its right-handed friends. 

You are given a sequence of strings.
You should join these strings into chunk of text where
the initial strings are separated by commas.
As a joke on the right handed robots,
you should replace all cases of the words "right" with the word "left",
even if it's a part of another word.
All strings are given in lowercase. 
'''

'''
1用字符串本身的replace方法
a.replace('word','python')
输出的结果是hello python

2用正则表达式来完成替换:
import re
strinfo = re.compile('word')
b = strinfo.sub('python',a)
print b
输出的结果也是hello python
'''

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    message = ''
    for i in phrases:
        message = ','.join([message ,i.replace('right', 'left')])
    return message[1:]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
