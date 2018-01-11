'''
一个类，要求增加、减少、查询功能
'''

class Friends:
    def __init__(self, connections):
        self.connections = []
        connections = list(connections)
        for _pairs in connections:
            self.connections.append(list(_pairs))

    def add(self, connection):
        connection = list(connection)
        _flag = True
        for _pairs in self.connections:
            if _pairs == connection or [_pairs[1], _pairs[0]] == connection:
                _flag = False
                break
        if _flag:
            self.connections = self.connections + [connection]
        return _flag

    def remove(self, connection):
        connection = list(connection)
        _flag = False
        for _pairs in self.connections:
            if _pairs == connection or [_pairs[1], _pairs[0]] == connection:
                _flag = True
                break
        if _flag:
            self.connections.remove(connection)
        return _flag

    def names(self):
        _name = []
        for _pairs in self.connections:
            _name.append(_pairs[0])
            _name.append(_pairs[1])
        return set(_name)

    def connected(self, name):
        _name = []
        for _pairs in self.connections:
            if name in _pairs:
                _name.append(_pairs[0])
                _name.append(_pairs[1])
                _name.remove(name)
        return set(_name)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

'''
class Friends:

    def __init__(self, connections):

        self.connections = list(connections)


    def add(self, connection):

        if self._inConnections(connection):

            return False

        self.connections.append(connection)

        return True


    def remove(self, connection):

        if not self._inConnections(connection):

            return False

        self.connections.remove(connection)

        return True


    def names(self):

        names = []

        for conn in self.connections:

            names += [name for name in conn if name not in names]

        return set(names)

        

    def connected(self, name):

        connected= []

        for conn in self.connections:

            if name in conn:

                conn.remove(name)

                connected.append(conn.pop())

        return set(connected)

        

    def _inConnections(self, connection):

        for oldConn in self.connections:

            if sorted(oldConn) == sorted(connection):

                return True

        return False

'''