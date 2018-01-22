def checkio(data):
    sumnumber = 0
    while data:
        sumnumber += data.pop()
    return sumnumber

if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'
    print('All ok')
