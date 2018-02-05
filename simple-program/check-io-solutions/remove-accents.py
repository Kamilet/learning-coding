ACIENTS = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a', 'ă': 'a',
           'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o', 'ớ': 'o',
           'ê': 'e', 'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
           'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
           'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
           'ǖ': 'u', 'ǘ': 'u', 'ǚ': 'u', 'ǜ': 'u', 'ü': 'u'}

import codecs


def checkio(in_string):
    "remove accents"
    in_string = list(in_string)
    for i in range(len(in_string)):
        if in_string[i] in ACIENTS:
            in_string[i] = ACIENTS[in_string[i]]
    return ''.join(in_string)

    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
