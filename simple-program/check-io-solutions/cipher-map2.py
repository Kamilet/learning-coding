'''
对位密码表
向右翻转4次
'''
def recall_password(cipher_grille, ciphered_password):
    password = [[],[],[],[]]
    cipher_grille = list(cipher_grille)
    ciphered_password = list(ciphered_password)
    for i in [0,1,2,3]:
        for k in [0,1,2,3]:
            if cipher_grille[i][k] == 'X':
                password[0].append(ciphered_password[i][k])
                password[1].append(ciphered_password[k][3-i])
                password[2].append(ciphered_password[3-i][3-k])
                password[3].append(ciphered_password[3-k][i])
    password[1] = [password[1][2], password[1][0], password[1][1], password[1][3]]
    password[3] = [password[3][3], password[3][2], password[3][0], password[3][1]]
    print(password[1],'!!!tfor')
    print(password[3],'!!!ddqd')
    print(''.join(password[0]+password[1]+password[2][::-1]+password[3]))
    return ''.join(password[0]+password[1]+password[2][::-1]+password[3])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
