
'''
看例子..
'''
COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(string):
    output = ''
    maxlen = 0
    if len(string) <= 39:
        maxlen = len(string)
        output = ''.join([' ', '_'*int((maxlen+2)), '\n< ',
                          string, ' >\n ', '-'*(maxlen+2), COW])
    else:
        newstring = []
        while len(string) >= 40:
            cut = string[:40]
            for i in range(len(cut)-1, -1, -1):
                if cut[i] == ' ':
                    newstring.append(cut[:i])
                    maxlen = max(len(cut[:i]), maxlen)
                    string = string[i+1:]
                    break
        maxlen = max(len(string), maxlen)
        newstring.append(string)
        string = ''
        for i in range(len(newstring)):
            if i == 0:
                string = ''.join(
                    [string, '/ ', newstring[i], ' '*(maxlen - len(newstring[i])), ' \\', '\n'])
            elif i == len(newstring)-1:
                string = ''.join([string, '\\ ', newstring[i],
                                  ' '*(maxlen - len(newstring[i])), ' /'])
            else:
                string = ''.join(
                    [string, '| ', newstring[i], ' '*(maxlen - len(newstring[i])), ' |', '\n'])
        output = ''.join(['\n ', '_'*(maxlen+2), '\n',
                          string, ' \n ', '-'*(maxlen+2), COW])
    print(r'{}'.format(output))
    return r'{}'.format(output)


cowsay('Checkio rulezz') == r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

'''

cowsay('A longtextwithonlyonespacetofittwolines.') == r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

'''

cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.') == r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
