'''
Numeral Value
I   1 (unus)
V   5 (quinque)
X   10 (decem)
L   50 (quinquaginta)
C   100 (centum)
D   500 (quingenti)
M   1,000 (mille)
'''

# This is failed written by me.
# retrying


def checkio(data):

    finlist = []
    #justlist:
    finlist.append(int(data/1000)*'M'+'M')
    finlist.append(int(data%1000/500)*'D'+'D')
    finlist.append(int(data%500/100)*'C'+'C')
    finlist.append(int(data%100/50)*'L'+'L')
    finlist.append(int(data%50/10)*'X'+'X')
    finlist.append(int(data%10/5)*'V'+'V')
    finlist.append(int(data%5)*'I'+'I')
    while '' in finlist:
        finlist.remove('')
    print(finlist)
    flag = True
    while flag:
        print('runing')
        flag = False
        for i in [6, 4, 2]:
            if len(finlist[i]) == 5 and finlist[i][2] == finlist[i][-1]:
                finlist[i] = finlist[i][-1]
                finlist[i-1] = finlist[i-1][:-1] + finlist[i][-1] + finlist[i-1][-1] *2
                flag = True
        print(finlist)
        for i in [5, 3, 1]:
            if len(finlist[i]) == 4:
                finlist[i] = finlist[i][-1]
                if len(finlist[i-1]) == 1:
                    finlist[i-1] = finlist[i+1][-1] + finlist[i-1]*2
                else:
                    finlist[i-1] = finlist[i-1][:-1] + finlist[i+1][-1] + finlist[i-1][-1] *2
                flag = True
        print(finlist)


    for i in range(0,7):
        finlist[i] = finlist[i][:-1]
    finlist = ''.join(finlist)
    print(finlist)

    return finlist

checkio(3888)
checkio(499)
checkio(76)
checkio(6)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio(3999) == 'MMMCMXCIX', '3999'
    assert checkio(579) == 'DLXXIX', '579'
