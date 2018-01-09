

def is_family(tree):
    # the full version will check the first pair of father and son in family
    # then use them as numbers of list:family, and tree.remove(first pair)
    # and check the tree[0]
    # if father in and son not, add son in family, tree.remove(tree[0])
    # if both not, tree.append(tree[0]) and tree.remove(tree[0]) to check them later
    # keep checking until no pair removed after a loop
    # then if len(tree) > 0, false
    # ---------------------
    # i thought that's good.. but for some reason and lagging my PC...
    # ---------------------
    # but this is simple version that i find it can local check successfully
    # in this situation:
    # [['logan', 'mike'], ['join', 'lisa'], ['mike', 'join']]
    # will return False, actually should return True rignt?
    # i need better iedas...
    '''
    tree.sort()
    family = tree[0]
    for f_s in tree[1:]:
        if f_s[0] in family and f_s[1] not in family:
            family.append(f_s[1])
        else:
            return False
    return True
    '''
    tree.sort()
    # son check, every one can be son just 1 time
    son = []
    for f_s in tree:
        son.append(f_s[1])
    if len(son) != len(set(son)):
        print('before loop, end: you can\'t be two man\'s son')
        return False
    # daddy check, every one should be daddy or have a daddy
    family = tree[0]
    tree = tree[1:]
    loop = 0
    while True:
        if loop > len(tree) or len(tree)==0:
            break
        if tree[0][0] in family and tree[0][1] not in family:
            family.append(tree[0][1])
            tree = tree[1:]
            loop = 0
        elif tree[0][1] in family and tree[0][0] not in family:
            family.append(tree[0][0])
            tree = tree[1:]
            loop = 0
        else:
            tree.append(tree[0])
            tree = tree[1:]
            loop += 1
    print('after loop, end, this left:',tree)
    return not len(tree)




if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'


    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([["Logan","Mike"],["Alexander","Jack"],["Jack","Logan"]]) == True, '!'
    assert is_family([["Logan","Mike"],["Alexander","Jack"],["Jack","Alexander"]]) == False, '!'
    assert is_family([["Logan","William"],["William","Jack"],["Jack","Mike"],["Mike","Alexander"]]) == True, '!'
    assert is_family([["Logan","William"],["Mike","Alexander"],["William","Alexander"]]) == False, '!'
    print("Looks like you know everything. It is time for 'Check'!")





'''
def is_family(tree):
    lentree = len(tree)
    if lentree == 1: return True
    family_map = []
    for i in range(lentree*2):
        family_map.append([])
    # we find the last pair of son and father.
    for i in range(lentree):
        trigger = False
        for t in range(lentree):
            if tree[i][0] in tree[t] or tree[i][1] in tree[t]:
                last_pair = i
                trigger = True
        if not trigger:
            return False
    family_map[lentree-1].append(tree[last_pair][0])
    family_map[lentree].append(tree[last_pair][1])
    lastop = [None,None]
    while True:
        trigger = False
        try:
            if tree[0][0] == lastop[0] and tree[0][1] == lastop[1]:
                return False
        except IndexError:
            break
        for t in range(lentree*2-1):
            if tree[0][0] in family_map[t]:
                family_map[t+1].append(tree[0][1])
                trigger = True
            if tree[0][1] in family_map[t]:
                family_map[t-1].append(tree[0][0])
                trigger = True
        lastop = tree[0][:]
        if not trigger:
            tree.append(tree[0])
        tree.remove(tree[0])
    family_cont = []
    for items in range(len(family_map)):
        if family_map[items] != []:
            _temp = list(set(family_map[items]))
            family_cont += _temp
    while True:
        if len(family_cont) == 0:
            return True
        if family_cont.pop() in family_cont:
            return False
'''

'''
def is_family(tree):
    family_dict = {}
    for items in tree:
        try:
            if items[1] in family_dict[items[0]]:
                pass
            else:
                family_dict[items[0]].append(items[1])
        except KeyError:
            family_dict[items[0]] = [items[1]]
    print(tree,'!!!!',family_dict)
    # 进行递归，在family_dict里取出key，去key里寻找，再去key的key里寻找，直到key不存在
    # 寻找的路径存入一个数组，如果已经存在，跳出
    
    return True
'''

'''
def is_family(tree):
    family = set(tree[0])
    for father, son in tree[1:]:
        if father in family and son not in family:
            family.add(son)
        else:
            return False
return True
'''

#def is_family(tree, flag = True):
    # the full version will check the first pair of father and son in family
    # then use them as numbers of list:family, and tree.remove(first pair)
    # and check the tree[0]
    # if father in and son not, add son in family, tree.remove(tree[0])
    # if both not, tree.append(tree[0]) and tree.remove(tree[0]) to check them later
    # keep checking until no pair removed after a loop
    # then if len(tree) > 0, false
    # ---------------------
    # i thought that's good.. but for some reason and lagging my PC...
    # ---------------------
    # but this is simple version that i find it can local check successfully
    # in this situation:
    # [['logan', 'mike'], ['join', 'lisa'], ['mike', 'join']]
    # will return False, actually should return True rignt?
    # i need better iedas...

'''
    family = tree[0]
    for f_s in tree[1:]:
        if f_s[0] in family and f_s[1] not in family:
            family.append(f_s[1])
        else:
            return False
    return True
    '''
    # so, the new one
    # ErrUchIsDown: You process has been killed because of using too much resources
    # again.. trying to add a trigger?

'''
    family = tree[0]
    tree = tree[1:] # changed fomr remove(tree[0])
    f_s=[None,None]
    trigger = 0
    maxstep = 1
    for i in range(len(tree)+1):
        maxstep *= (i+1)
    while True:
        trigger += 1
        try:
            if f_s[0] == tree[0][0] and f_s[1] == tree[0][1]:  # changed fomr f_s = tree[0]
                return False
        except IndexError:
            print('out')
            return True
        f_s = [tree[0][0], tree[0][1]]
        if f_s[0] in family and f_s[1] not in family:
            family.append(f_s[1])
            tree = tree[1:]  # changed fomr remove(tree[0])
        else:
            tree.append(f_s)
            tree = tree[1:]  # changed fomr remove(tree[0])
        if trigger > maxstep:
            print('out1')
            return False
    return True
'''