'''
替换游戏，一次一个

没解决
'''
PASSLIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60,
            70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900]


def checkio(given_numbers):
    '''work here'''
    end = given_numbers[-1]
    now = given_numbers[0]
    rest = given_numbers[1:]
    route = [now]
    retrycount = 1
    while now != end:
        print(now)
        for num in rest:
            if abs(now - num) in PASSLIST:
                now = num
                route.append(now)
                rest.remove(now)
                retrycount = 1
                break
            retrycount += 1
            rest = given_numbers[1:]
            try:
                rest.remove(route[1:retrycount])
            except:
                pass
            route = [given_numbers[0]]
    print(route)


def findroute(number, numbers):
    return_list = []
    for num in numbers:
        if abs(number - num) in PASSLIST:
            return_list.append(num)
    return return_list


checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [
    123, 121, 921, 991, 999]
checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [
    111, 121, 127, 727, 777]
checkio([456, 455, 454, 356, 656, 654]) == [
    456, 454, 654]  # or [456, 656, 654]

print(findroute(123, [123, 991, 323, 321, 329, 121, 921, 125, 999]))
