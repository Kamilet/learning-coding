VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

import re

def checkio(text):
    number = 0
    text = re.split('\n|,| |\.',text.upper())
    for letters in text:
        if len(letters) > 1:
            for alpha in range(1, len(letters)):
                if letters[alpha].isdigit() or letters[alpha-1].isdigit():
                    _temp = False
                    break
                elif letters[alpha] in VOWELS and letters[alpha-1] in VOWELS:
                    _temp = False
                    break
                elif letters[alpha] in CONSONANTS and letters[alpha-1] in CONSONANTS:
                    _temp = False
                    break
                else:
                    _temp = True
            number += _temp
    print(number)
    return number

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?") == 8
