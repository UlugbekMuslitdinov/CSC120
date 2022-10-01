class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    # getter for the _value attribute
    def value(self):
        return self._value

    # getter for the _next attribute
    def next(self):
        return self._next

    def __str__(self):
        return str(self._value) + "; "


class LinkedList:
    def __init__(self):
        self._head = None

    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node

    def sum(self):
        curr_node = self._head
        total = 0
        while curr_node is not None:
            total += curr_node.value()
            curr_node = curr_node.next()
        return total

    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node

    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2

    def find(self, value):
        curr_node = self._head
        while curr_node != None:
            if curr_node.value() == value:
                return True
            curr_node = curr_node.next()
        return False

    def sort(self):
        curr_node = self._head
        while curr_node != None:
            next = curr_node.next()
            while next != None:
                if curr_node.value() > next.value():
                    self.insert(self, self.remove(next), curr_node)
                next = next.next()
            curr_node = curr_node.next()



    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string
