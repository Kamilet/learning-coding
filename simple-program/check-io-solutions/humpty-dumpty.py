'''
计算椭球的体积和表面积
'''

def checkio(height, width):
    '''height是拉长，width是半径，返回表面积和体积'''
    from math import pi
    volume = 4*pi/3 * (width/2)**3 * height/width
    # 椭球的近似表面积
    # surface_area = pi/3 * (width**2+width*height*2)
    # 球体的表面积，拉长
    # surface_area = pi * width**2 * (height/width)**(2/3)
    if height == width:
        # 球体的表面积
        surface_area = pi * width**2
    # 新的公式..
    # 不学数学就是不行
    # http://mathworld.wolfram.com/ProlateSpheroid.html
    elif height < width:
        import math
        e = math.sqrt(1 - height**2 / width**2)
        surface_area = 0.5 * pi  * (width**2) * (1 + (1-e**2)/e * math.atanh(e))
    else:
        import math
        e = math.sqrt(1 - width**2 / height**2)
        surface_area = 0.5 * pi * width ** 2 + 0.5 * pi * width * height / e * math.asin(e)

    return [round(volume,2), round(surface_area,2)]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"