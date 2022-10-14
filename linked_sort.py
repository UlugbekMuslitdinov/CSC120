class Node:

    def __init__(self, value):
        self._value = value
        self._next = None

    def __str__(self):
        return str(self._value)

    def set_next(self, target):
        self._next = target


class LinkedList:

    def __init__(self):
        self._head = None

    def add(self, node):
        node.set_next(self._head)
        self._head = node

    def add_between(self, node1, node2):
        node2.set_next(node1._next)
        node1.set_next(node2)

    def rm_from_hd(self):
        if self._head is None:
            return
        self._head = self._head._next

    def sort(self):
        # sort the linked list in descending order by value
        current = self._head
        sorted =[current]
        current = current._next
        while current is not None:
            for i in range(len(sorted)):
                if current._value > sorted[i]._value:
                    sorted.insert(i, current)
                    break
            else:
                sorted.append(current)
            current = current._next
        self._head = sorted[0]
        for i in range(len(sorted) - 1):
            sorted[i].set_next(sorted[i + 1])
        sorted[-1].set_next(None)




    def __str__(self):
        current = self._head
        result = ""
        while current is not None:
            result += str(current._value) + " "
            current = current._next
        return result


a = LinkedList()
a.add(Node(1))
a.add(Node(25))
a.add(Node(18))
a.add(Node(44))
print(a)
a.sort()
print(a)
