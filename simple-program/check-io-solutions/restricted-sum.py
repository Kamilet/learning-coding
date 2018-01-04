'''
The list of banned words are as follows:

    sum
    import
    for
    while
    reduce
'''



def checkio(data):
    global number
    number = 0
    plus(data)
    return number

def plus(data):
    global number
    #print('srart with:{}'.format(number),'len:',len(data))
    if len(data) > 0:
        number += data.pop()
        plus(data)
    #print('end with:{}'.format(number))





print('!!!!!!!!!!!!!!!!!',checkio([1,2,3]))