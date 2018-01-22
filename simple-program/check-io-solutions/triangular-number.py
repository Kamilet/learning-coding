'''
生成三角数
'''

def gen_triangular_number(limit):
    numbers = [0]
    height = 1
    while numbers[-1] <= limit:
        numbers.append(numbers[-1]+height)
        height+=1
    return numbers

print(gen_triangular_number(1000))