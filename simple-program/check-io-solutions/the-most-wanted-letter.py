'''
读取一段字符，返回最多的一个字母（小写）
若最多的有多个，则返回字典最前面的
'''

def checkio(text):
    # the most wanted letter
    dic_text = {}
    text = text.lower()
    for i in range(0, len(text)):
        if text[i] in ',.!? +-*/1234567890':
            continue
        try:
            dic_text[text[i]] = dic_text[text[i]] + 1
        except KeyError:
            dic_text[text[i]] = 1
    return sorted(dic_text.items(), key=lambda i: (-i[1], i[0]))[0][0]


'''
import string


def checkio(text):

    """

    We iterate through latyn alphabet and count each letter in the text.

    Then 'max' selects the most frequent letter.

    For the case when we have several equal letter,

    'max' selects the first from they.

    """

    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)
'''

'''
from collections import Counter


def checkio(text):

    count = Counter([x for x in text.lower() if x.isalpha()])

    m = max(count.values())

    return sorted([x for (x, y) in count.items() if y == m])[0]
'''

'''
import collections

def checkio(text):

    freq_list = collections.Counter(filter(str.isalpha, text.lower())).most_common()

    most_freq_count = max(freq[1] for freq in freq_list)

    return sorted([freq[0] for freq in freq_list if freq[1] == most_freq_count])[0]
'''

'''
def checkio(text):

    s = list(text.lower())

    letters = [s.count(chr(x)) for x in range(97,123)]



    return chr(97+letters.index(max(letters)))
'''