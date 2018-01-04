'''
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters.
You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession. 
'''

def checkio(words):
    words = words.split(' ')
    count = 0
    _count = 0
    for i in words:
        if not i.isdigit():
            _count += 1
            if _count > count:
                count = _count
        else:
            _count = 0
    return count > 2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
