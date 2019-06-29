'''
写出从#000000到#FFFFFF变化的SVG。

注意，高渲染消耗！

注意，2^24种颜色！

注意，卡死不要怪我！
'''

import os
fileHead = '<?xml version="1.0" encoding="utf-8"?>\n\
<!-- Generator: Adobe Illustrator 16.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n\
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n\
<svg version="1.1" id="Kamilet.cn 设计师充电站" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\n\
     width="8192px" height="8192px" viewBox="0 0 8192 8192" enable-background="new 0 0 8192 8192" xml:space="preserve">'
fileFoot = '</svg>'
clip1 = '\n<linearGradient id="SVGID_'
clip2 = 0 #svgId countNumber
clip3 = '_" gradientUnits="userSpaceOnUse" x1="'
clip4 = 0 #position-x1
clip5 = '" y1="'
clip6 = 0 #position-y1
clip7 = '" x2="'
clip8 = 0 #position-x2
clip9 = '" y2="'
#clip10 = 0 #position-y2 = position-y1
clip11 = '">\n\
    <stop  offset="0" style="stop-color:#'
clip12 = 0 #gradientStart
clip13 = '"/>\n\
    <stop  offset="1" style="stop-color:#'
clip14 = 0 #gradientEnd
clip15 = '"/>\n\
</linearGradient>\
'
clip16 = '\n<rect x="'
clip17 = 0 #rect-x
clip18 = '" y="'
clip19 = 0 #rect-y
clip20 = '" fill="url(#SVGID_'
#clip21 = 0 #svgId
clip22 = '_)" width="32" height="32"/>\
'
tempClip12 = '1'
tempClip14 = '2'
def writeGo(filename):
    global clip2, clip4, clip6, clip8, clip12, clip14, clip17, clip19
    names = locals()
    writeFile = open(filename, 'w', encoding='utf-8')
    writeFile.write(fileHead)
    #main
    for i in range(0,65536):
        #define svgID
        clip2 = i+1
        #define rect-x and rect -y
        clip17 = i%256 * 32
        clip19 = int(i/256)%256 * 32
        #define gradient Start and End
        clip12 = 256*i
        clip14 = 256*(i+1)-1
        #define position-y1 y2
        clip6 = 16+i*32
        #define position-x1 x2
        clip4 = clip17
        clip8 = clip4+32
        writeFile.write(letsWrite())
    writeFile.write(fileFoot)
    writeFile.close()

def letsWrite():
    tempClip12 = '0'*(6-len(hex(clip12)[2:]))+hex(clip12)[2:]
    tempClip14 = '0'*(6-len(hex(clip14)[2:]))+hex(clip14)[2:]
    return clip1+str(clip2)+clip3+str(clip4)+clip5+str(clip6)+clip7+str(clip8)+clip9+str(clip6)+clip11\
+tempClip12+clip13+tempClip14+clip15+clip16+str(clip17)+clip18+str(clip19)+clip20+str(clip2)+clip22

writeGo('super-gradient.svg')