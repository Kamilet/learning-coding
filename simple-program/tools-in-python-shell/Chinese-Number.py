'''转化阿拉伯数字为汉字数字'''
# 理论处理极限：一万亿以内
# 小数部分处理极限：分
# 从最大的数开始，后面全部补零（为了填发票）
NUMBER_CHT = {1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍',
              6: '陆', 7: '柒', 8: '捌', 9: '玖', 0: '零'}


def chn_num(number):
    part_XIAOSHU = part_WAN = part_YI = part_WANYI = 0
    if number != int(number):
        part_XIAOSHU = int((number - int(number))*100)
        number = int(number)
    if number or part_XIAOSHU:
        part_WAN = number % 10000
        if number >= 10000:
            part_YI = number//10000
            if number >= 10000**2:
                part_WANYI = number//(10000**2)
                if number >= 10000**3:
                    print('数据溢出')
                    return
    else:
        print('零'*20)
        return
    parts = [part_WANYI, part_YI, part_WAN]
    # print(parts)
    # print(part_XIAOSHU)
    chn_number = []
    _switch = False
    for i in [0, 1, 2]:
        _temppart = []
        if not _switch and not parts[i]:
            continue
        if parts[i] >= 1000 or _switch:
            _temppart.append(NUMBER_CHT[parts[i]//1000])
            _temppart.append('仟')
            _switch = True
        if parts[i] % 1000 >= 100 or _switch:
            _temppart.append(NUMBER_CHT[(parts[i] % 1000)//100])
            _temppart.append('佰')
            _switch = True
        if parts[i] % 100 >= 10 or _switch:
            _temppart.append(NUMBER_CHT[(parts[i] % 100)//10])
            _temppart.append('拾')
            _switch = True
        if parts[i] % 10 >= 1 or _switch:
            _temppart.append(NUMBER_CHT[(parts[i] % 10)])
            _switch = True
        if i == 0:
            _temppart.append('亿')
        elif i == 1:
            _temppart.append('万')
        else:
            _temppart.append('圆')
        chn_number += _temppart
    if part_XIAOSHU:
        if part_XIAOSHU >= 10 or _switch:
            chn_number += [NUMBER_CHT[part_XIAOSHU//10], '角']
            _switch = True
        if part_XIAOSHU % 10 >= 0 or _switch:
            chn_number += [NUMBER_CHT[part_XIAOSHU % 10], '分']
    else:
        chn_number.append('整')
    print(' | '.join(chn_number))

while True:
    you_are_beautiful_you_are_lovely = input('input a number between 0 to 10^12:\n')
    if type(you_are_beautiful_you_are_lovely) is int or\
       type(you_are_beautiful_you_are_lovely) is float:
       chn_num(you_are_beautiful_you_are_lovely)
    else:
        input('wrong input..exit..')
        break

# 以下待开发
'''
阿拉伯数字转中文数字，阿拉伯数字转中文书面数字（繁体）。
中文数字转阿拉伯数字，中文书面数字转阿拉伯数字。
解决填发票等场合下需要写书面数字的问题。
力求一个class解决。
壹   贰   叁   肆   伍   陆   柒   捌
十   百   千   万   亿   元
玖   零   拾   佰   仟   万   亿   圆
'''
'''
NUMBER_CHS = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五',
              '6': '六', '7': '七', '8': '八', '9': '九', '10': '十',
              '100': '百', '1000': '千', '10000': '万', '100000000': '亿',
              '0': '零', 'RMB': '元'}
NUMBER_CHT = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍',
              '6': '陆', '7': '柒', '8': '捌', '9': '玖', '10': '拾',
              '100': '佰', '1000': '仟', '10000': '万', '100000000': '亿',
              '0': '零', 'RMB': '圆'}
NUMBER_NUM = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
              '6': '6', '7': '7', '8': '8', '9': '9', '0': '0'}


class chineseNumber(self, number):
    number = str(number)
    if number.isdigit():
        self.number = number
    else:
        if number[0] in NUMBER_CHS.values():
            self.number = self.chs_2_num(number)
        elif number[0] in NUMBER_CHT.values():
            self.number = self.cht_2_num(number)
        else:
            print('抱歉，您输入的数字不合法')

    def chs_2_num(NUMBER):
        NUMBER_TURN_CHS = {value:key for key, value in NUMBER_CHS.items()}
        pass

    def cht_2_num(NUMBER):
        pass
'''
