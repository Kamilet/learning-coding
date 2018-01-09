'''
判断字符串1是否由字符串2排列组合而来
'''

def verify_anagrams(first_word, second_word):
    first_word = list(first_word.lower())
    second_word = list(second_word.lower())
    first_word_copy = first_word[:]
    while ' ' in first_word:
        first_word.remove(' ')
        first_word_copy.remove(' ')
    while ' ' in second_word:
        second_word.remove(' ')
    for i in first_word:
        if i in second_word:
            first_word_copy.remove(i)
            second_word.remove(i)
    return not (len(first_word_copy) or len(second_word))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
    assert verify_anagrams("Kings Lead Hat", "Talking Heads") == True, '123'

