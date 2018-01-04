'''
检查括号是否正确
'''




def checkio(expression):
    x = ''
    for i in range(len(expression)):
        if expression[i] in '{[()]}':
            a = expression[i]
            x = ','.join([x, expression[i]])
    x = x.split(',')
    flag = True
    dic = {'{':'x1','[':'x2','(':'x3','}':'{',']':'[',')':'(','':''}
    while flag:
        flag = False
        for i in range(1, len(x)):
            if x[i-1] != '' and x[i-1] == dic[x[i]]:
                x[i-1] = x[i] = ''
                flag = True
                break
        while '' in x:
            x.remove('')
    if len(x) == 0:
        return True
    else: return False







#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("([()])") == True, "My"
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

'''
brackets = (('(', ')'), ('{', '}'), ('[', ']'))

def checkio(expression):

    last = []

    for i in expression:

        if i in '({[':

            last += [i]

        if i in ')}]':

            if not last or (last.pop(), i) not in brackets:

                return False

    return not last
'''