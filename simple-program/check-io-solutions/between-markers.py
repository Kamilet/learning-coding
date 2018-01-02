'''
返还两个特定字符之间的值
'''
#import re

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    '''
    if not begin in text:
        begin = ''
    if not end in text:
        end = ''
    '''
    #这一段没能完成工作，总是会多出方括号不知道为什么
    '''
    try:
        content = re.compile(begin + '(.*?)' + end,re.S).findall(text)[0]
        print(content)
        return content
    except:
        return text
    '''
    startindex = 0
    endindex = len(text)
    if begin in text:
        startindex = text.index(begin) + len(begin)
    if end in text:
        endindex = text.index(end)
    print(text[startindex:endindex])
    return text[startindex:endindex]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
