def checkio(opacity):
    bfnq_0 = 1
    bfnq_1 = 1
    opc = 0

    for i in range(1, 5000):
        if opacity == 10000 - opc:
            print(i-1,'!',opacity)
            return i - 1

        if bfnq_1 == i:
            opc += bfnq_1
            bfnq_0, bfnq_1 = bfnq_1, bfnq_1 + bfnq_0
        else:
            opc -= 1


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"