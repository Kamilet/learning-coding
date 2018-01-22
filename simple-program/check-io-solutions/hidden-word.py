'''扫描特定内容，返回位置'''

def checkio(string, word):
    string = string.split('\n')
    for line in range(len(string)):
        string[line] = ''.join(string[line].split(' ')).lower()
    print(string)
    flag = False
    retry = False
    for x in range(len(string)):
        for y in range(len(string[x])):
            if string[x][y] == word[0]:
                flag = True
                retry = False
                for i in range(1,len(word)):
                    try:
                        if string[x+i][y] != word[i]:
                            retry = True
                            break
                    except IndexError:
                        retry = True
                if retry:
                    for i in range(1,len(word)):
                        try:
                            if string[x][y+i] != word[i]:
                                flag = False
                        except IndexError:
                            flag = False
            if flag: break
        if flag: break
    if retry:
        print([x+1,y+1,x+1,y+len(word)])
        return [x+1,y+1,x+1,y+len(word)]
    else:
        print([x+1,y+1,x+len(word),y+1])
        return [x+1,y+1,x+len(word),y+1]


checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]

checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]

checkio("Hi all!\nAnd all goodbye!\nOf course goodbye.\nor not","haoo")