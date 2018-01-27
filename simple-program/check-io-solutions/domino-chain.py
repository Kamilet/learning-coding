'''
数链条
'''


def domino_chain(chain):
    chain = chain.split(', ')
    # sort and arrange
    for i in range(len(chain)):
        chain[i] = chain[i].split('-')
        chain[i][0], chain[i][1] = int(chain[i][0]), int(chain[i][1])
        if chain[i][0] > chain[i][1]:
            chain[i][0], chain[i][1] = chain[i][1], chain[i][0]
    # print(new_chain)
    # combine
    flag = True
    while flag:
        flag = False
        new_chain = sorted(chain, key = lambda x:(x[0], x[1]))
        for i in range(1, len(new_chain)):
            if new_chain[i][0]-1 <= new_chain[i-1][1]:
                chain.remove(new_chain[i])
                chain.remove(new_chain[i-1])
                chain.append([new_chain[i-1][0], max(new_chain[i-1][1], new_chain[i][1])])
                flag = True
                break
    print(chain)
    return len(chain)


domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 1
domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4, 7-8, 9-10, 11-15, 17-18") == 1

