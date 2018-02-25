'''
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are uppercase,
and/or ends by at least 3 exclamation marks and/or contains
at least one of the following “red” words "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways -
"HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP" 
'''
RED_WORDS = ['red', 'help', 'asap', 'urgent']
PARA = ['!','-','.',',']

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    # check for uppercase
    if subj.isupper():
        return True
    # check for 3 exclamation marks
    if len(subj)>=3 and subj[-3:] == '!!!':
        return True
    # check for red words
    subj = subj.lower()
    subj = subj.split(' ')
    import re
    for word in subj:
        word_temp = list(word)
        for i in range(len(word_temp)-1):
            if word_temp[i] == word_temp[i+1]:
                word_temp[i] = '.'
        for para in PARA:
            while para in word_temp:
                word_temp.remove(para)
        word_temp = ''.join(word_temp)
        print(word_temp)
        if word_temp in RED_WORDS:
            return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("We need you A.S.A.P.!!") == True
    assert is_stressful('where are you?!!!!') == True
    assert is_stressful('UUUURGGGEEEEENT here') == True
    print('Done! Go Check it!')