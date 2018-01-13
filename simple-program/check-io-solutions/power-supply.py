def power_supply(network, power_plants):
    # 字典每一个p向外检查n次（距离）
    # 有一端在列表里，砍掉
    # 砍完所有字典，剩下的全部合到一起set抛出
    # 特别处理n=0的情况即可
    _templine_big = list(power_plants.keys())
    power_plants = sorted(power_plants.items(), key = lambda x:x[1], reverse=True)
    for stations in power_plants:
        _templine = [stations[0]]
        if stations[1]:
            for times in range(stations[1]):
                _templine_1 = []
                for links in range(len(network)):
                    # print(_templine)
                    if network[links][0] in _templine and network[links][0] != '':
                        _templine_1.append(network[links][1])
                        network[links] = ['','']
                    if network[links][1] in _templine and network[links][1] != '':
                        _templine_1.append(network[links][0])
                        network[links] = ['','']
                    # print(network,'ntw')
                _templine = _templine + _templine_1
                _templine_big = _templine_big + _templine
        else:
            for links in network:
                if stations in links:
                    links.remove(stations)
                    links.append('')
    for links in range(len(network)):
        if network[links][0] != '' and network[links][0] in _templine_big:
            network[links] = ['',network[links][1]]
        if network[links][1] != '' and network[links][1] in _templine_big:
             network[links] = [network[links][0],'']
    # print(_templine_big,'clear')
    # print(network)
    unpowered = []
    for items in network:
        if items[0] != '':
            unpowered.append(items[0])
        if items[1] != '':
            unpowered.append(items[1])
    # print(unpowered,'result')
    return set(unpowered)

if __name__ == '__main__':

    assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['c2']), 'one blackout'
    assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3']), 'two blackout'
    assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([]), 'no blackout'
    assert power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0}) == set(['c0', 'c2']), 'weak power-plant'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}) == set([]), 'cooperation'
    assert power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
                         ['c5', 'c6'], ['c5', 'p7']],
                        {'p1': 1, 'p7': 1}) == set(['c3', 'c4', 'c6']), 'complex cities 1'

    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
                         ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
                       ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
                       ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
                      {'p0': 1, 'p12': 4, 'p8': 1}) == set(['c6', 'c7']), 'complex cities 2'
    assert power_supply([['c1', 'c2'], ['c2', 'c3']], {}) == set(['c1', 'c2', 'c3']), 'no power plants'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}) == set(['c3']), 'circle'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}) == set([]), 'more than enough'
    assert power_supply([["c1","p1"],["p1","p2"]],{"c1":1}) == set(['p2'])
    print("Looks like you know everything. It is time for 'Check'!")


'''思路错误，每个发电站为起点不仅一条线
def power_supply(network, power_plants):
    power_line = []
    flag = True
    for stations in power_plants:
        power_line.append([stations])
    for num in range(len(power_line)):
        i = 0
        retry = 0
        while flag:
            flag = False
            if i >= len(power_line[num]) or len(network) == 0 or retry > len(power_line[num]):
                break
            if network[0][0] == power_line[num][i]:
                power_line[num].append(network[0][1])
                network.remove(network[0])
                retry = 0
                i += 1
                flag = True
            elif network[0][1] == power_line[num][i]:
                power_line[num].append(network[0][0])
                network.remove(network[0])
                flag = True
                retry = 0
                i += 1
            else:
                _first = network[0][0]
                network.append(network[0])
                network = network[1:]
                if _first != network[0][0]:
                    flag = True
                    retry += 1
    unlinked = []
    for num in power_line:
        unlinked = unlinked + num[power_plants[num[0]]+1:]
    print(power_line)
    print(unlinked)
    return set(unlinked)
    '''

'''思路不对，跳出卡循环
def power_supply(network, power_plants):
    power_line = []
    for stations in power_plants:
        power_line.append({0:[stations]})
    retry = 0
    while len(network):
        if retry > len(network) + 100:
            print('retry exit')
            break
        for i in range(len(power_line)):
            for level in range(len(power_line[i])):
                if network[0][0] in power_line[i][level]:
                    try:
                        power_line[i][level+1] = power_line[i][level+1] + [network[0][1]]
                    except:
                        power_line[i][level+1] = [network[0][1]]
                    network = network[1:]
                    retry = 0
                elif network[0][1] in power_line[i][level]:
                    try:
                        power_line[i][level+1] = power_line[i][level+1] + [network[0][0]]
                    except:
                        power_line[i][level+1] = [network[0][0]]
                    network = network[1:]
                    retry = 0
                else:
                    network.append(network[0])
                    network = network[1:]
                    retry += 1
    print(power_line)
    '''