'''
国际象棋，卒在
给出数值在这样的棋盘上，看看哪些是安全的：
 a b c d e f g h
8
7
6
5
4
3
2
1
'''
def safe_pawns(pawns):
    _safe = 0
    for i in pawns:
        if chr(ord(i[0])+1)+str(int(i[1])-1) in pawns:
            _safe += 1
        elif chr(ord(i[0])-1)+str(int(i[1])-1) in pawns:
            _safe += 1
    return _safe


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
