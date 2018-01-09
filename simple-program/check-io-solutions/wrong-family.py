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
    print("Looks like you know everything. It is time for 'Check'!")

    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
