def checkme(ox, game_result):
    if ox in game_result:
        return True
    for i in [0, 1, 2]:
        if ox == game_result[0][i]+game_result[1][i]+game_result[2][i]:
            return True
    if ox == game_result[0][0]+game_result[1][1]+game_result[2][2]:
        return True
    if ox == game_result[0][2]+game_result[1][1]+game_result[2][0]:
        return True
    return False

def checkio(game_result):
    if checkme('XXX', game_result):
        flag = 'X'
    elif checkme('OOO', game_result):
        flag = 'O'
    else:
        flag = 'D'
    return flag

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

