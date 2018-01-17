'''
读数字
'''
DICT_CARRY = {3:'ZERO', 2:'thousand', 1:'million', 0:'billion'}
DICT_NUMBER_WORD = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
               8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
               14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
               19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',
               60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'one hundred',
               0:'ZERO'}
DICT_NUMBER_FRIENDLY = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',
                        11:'11',12:'12',13:'13',14:'14',15:'15',16:'16',17:'17',18:'18',
                        19:'19',20:'20',21:'21',22:'22',23:'23',24:'24',25:'25',26:'26',
                        27:'27',28:'28',29:'29',30:'30',31:'31',32:'32',33:'33',34:'34',
                        35:'35',36:'36',37:'37',38:'38',39:'39',40:'40',41:'41',42:'42',
                        43:'43',44:'44',45:'45',46:'46',47:'47',48:'48',49:'49',50:'50',
                        51:'51',52:'52',53:'53',54:'54',55:'55',56:'56',57:'57',58:'58',
                        59:'59',60:'60',61:'61',62:'62',63:'63',64:'64',65:'65',66:'66',
                        67:'67',68:'68',69:'69',70:'70',71:'71',72:'72',73:'73',74:'74',
                        75:'75',76:'76',77:'77',78:'78',79:'79',80:'80',81:'81',82:'82',
                        83:'83',84:'84',85:'85',86:'86',87:'87',88:'88',89:'89',90:'90',
                        91:'91',92:'92',93:'93',94:'94',95:'95',96:'96',97:'97',98:'98',
                        99:'99',100:'1 hundred',0:'ZERO'}


def checkio(number, adds=False, friendly=False):
    if friendly:
        DICT_NUMBER = DICT_NUMBER_FRIENDLY
    else:
        DICT_NUMBER = DICT_NUMBER_WORD
    if number in DICT_NUMBER:
        return DICT_NUMBER[number]
    beautiful_voice_speaking = []
    part_thousand = part_million = part_billion = part_trillion = 0
    if number>0:
        part_thousand = number%1000
        if number>=1000:
            part_million = (number//1000)%1000
            if number>=1000**2:
                part_billion = (number//1000000)%1000
                if number>=1000**3:
                    part_trillion = (number//1000000000)%1000
                    if number>=1000**4:
                        print('You number {} is toooooo large!'.format(number))
                        input()
                        return None
    else: return 'zero'
    parts = [part_trillion, part_billion, part_million, part_thousand]
    for i in range(0,4):
        if not parts[i]:
            continue
        beautiful_voice_clip = []
        if parts[i] >= 100:
            beautiful_voice_clip.append(DICT_NUMBER[parts[i]//100])
            if adds and parts[i] >= 200:
                beautiful_voice_clip.append('hundreds')
            else:
                beautiful_voice_clip.append('hundred')
        if parts[i]%100 in DICT_NUMBER:
            beautiful_voice_clip.append(DICT_NUMBER[parts[i]%100])
        else:
            if parts[i]%100 >= 10:
                beautiful_voice_clip.append(DICT_NUMBER[((parts[i]%100)//10)*10])
            beautiful_voice_clip.append(DICT_NUMBER[parts[i]%10])
        if parts[i] > 0:
            if adds and parts[i]>1:
                beautiful_voice_clip.append(DICT_CARRY[i]+'s')
            else:
                beautiful_voice_clip.append(DICT_CARRY[i])
        if i!=3 and not friendly:
            beautiful_voice_clip.append('and')
        beautiful_voice_speaking += beautiful_voice_clip
    while 'ZERO' in beautiful_voice_speaking:
        beautiful_voice_speaking.remove('ZERO')
    if adds:
        while 'ZEROs' in beautiful_voice_speaking:
            beautiful_voice_speaking.remove('ZEROs')
    if beautiful_voice_speaking[-1] == 'and':
        beautiful_voice_speaking = beautiful_voice_speaking[:-1]
    # print(beautiful_voice_speaking)
    return ' '.join(beautiful_voice_speaking)






assert checkio(4)=='four'
assert checkio(143)=='one hundred forty three'
assert checkio(12)=='twelve'
assert checkio(101)=='one hundred one'
assert checkio(212)=='two hundred twelve'
assert checkio(40)=='forty'
# add 'and' between every four carrys
assert checkio(1143)=='one thousand and one hundred forty three'
assert checkio(2001143)=='two million and one thousand and one hundred forty three'
# the biggest number can rightly deal with
assert checkio(999999999999)=='nine hundred ninety nine billion and nine hundred ninety nine million and nine hundred ninety nine thousand and nine hundred ninety nine'
# set the 'adds' to True will add 's' for carrys
assert checkio(212,adds=True)=='two hundreds twelve'