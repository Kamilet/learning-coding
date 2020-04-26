'''针对Bilibili视频，使用av号或BV号，生成av+bv+cid形式，以方便提前发布预览页面。

生成结果样例（用于iframe的src）：
//player.bilibili.com/player.html?aid=625482865&amp;bvid=BV1kt4y1y7f9&amp;cid=182295773&amp;page=1

目前使用4月26日的规则。

可以用一下内容测试：
av625482865
BV1kt4y1y7f9

理论输出：
//player.bilibili.com/player.html?aid=625482865&amp;bvid=BV1kt4y1y7f9&amp;cid=182295773&amp;page=1
'''

import requests

# 密码表
alphabet = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
# cid查询url
cidUrl = 'https://www.bilibili.com/widget/getPageList?aid='

def code_b2a(bvcode):
    # bv到av
    r = 0
    for i, v in enumerate([11, 10, 3, 8, 4, 6]):
        r += alphabet.find(bvcode[v]) * 58**i
    return str((r - 0x2_0840_07c0) ^ 0x0a93_b324)

def code_a2b(avcode):
    # av到bv
    avcode = int(avcode[2:])
    avcode = (avcode ^ 0x0a93_b324) + 0x2_0840_07c0
    r = list('BV1**4*1*7**')
    for v in [11, 10, 3, 8, 4, 6]:
        avcode, d = divmod(avcode, 58)
        r[v] = alphabet[d]
    return ''.join(r)

def get_cid(avcode):
    # 用av号在线获取cid
    htmlText = requests.get(cidUrl+avcode[2:])
    # 检查视频是否可见，不可见时无法查询cid
    try:
        htmlText = eval(htmlText.content.decode('gbk', errors='ignore')[1:-1])['cid']
    except:
        flag = 1
        htmlText='0'
    else:
        flag = 0
    return [flag, htmlText]
    
kami = input('输入av号或BV号（需要带上前面的av或BV）：\n')
if kami[:2] == 'av' or kami[:2] == 'AV':
    cid = get_cid(kami)
    if cid[0] == 0:
        otpt = '//player.bilibili.com/player.html?aid='+kami[2:]+'&amp;bvid='\
        +code_a2b(kami)+'&amp;cid='+str(cid[1])+'&amp;page=1'
    else:
        otpt = '//player.bilibili.com/player.html?aid='+kami[2:]+'&amp;bvid='\
        +code_a2b(kami)+'&amp;page=1'
        print('无法打开视频页面，无法正常获取cid！')

elif kami[:2] == 'BV':
    avcode = code_b2a(kami)
    cid = get_cid('av'+avcode)
    if cid[0] == 0:
        otpt = '//player.bilibili.com/player.html?aid='+avcode+'&amp;bvid='\
        +kami+'&amp;cid='+str(cid[1])+'&amp;page=1'
    else:
        otpt = '//player.bilibili.com/player.html?aid='+avcode+'&amp;bvid='\
        +kami+'&amp;page=1'
        print('无法打开视频页面，无法正常获取cid！')
else:
    otpt = '输入错误！'
print(otpt)
