'''
密码长度大于10
至少有1大写、1小写、1数字
返回布尔类型的值
'''

def checkio(data):
    
    flag1 = flag2 = flag3 = 0

    for i in range(0, len(data)):
        flag1 += data[i] >= 'A' and data[i] <= 'Z'
        flag2 += data[i] >= 'a' and data[i] <= 'z'
        flag3 += data[i] >= '0' and data[i] <= '9'

    #replace this for solution
    return bool(len(data)>=10 and flag1 and flag2 and flag3)

#Some hints
#Just check all conditions

#笔记：string.islover() 可以在和数字混编的时候返回
#print('A1231!,,,,|!4'.isupper())

'''
def checkio_other(data):
	print(not (len(data) < 10))
	print(data.isdigit())
	print(data.isalpha())
	print(data.islower())
	print(data.isupper())
	return not (len(data) < 10) |  data.isdigit() | data.isalpha() | data.islower() | data.isupper()
'''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
return not (len(data) < 10) |  data.isdigit() | data.isalpha() | data.islower() | data.isupper()
'''