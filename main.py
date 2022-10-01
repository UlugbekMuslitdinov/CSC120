class LinkedList:
    def __init__(self):
        self._head = None

    def add(self, new):
        new._next = self._head
        self._head = new

    def print_elements(self):
        current = self._head
        while current != None:
            print(str(current._value))
            current = current._next

    # define this
    def incr(self):
        current = self._head
        while current != None:
            current._value += 1
            current = current._next

    # define this
    def linkedlist_to_plist(self):
        list_return = []
        current = self._head
        while current != None:
            list_return.append(current._value)
            current = current._next
        return list_return

    # define this
    def remove_first(self):
        if self._head != None:
            n = self._head
            self._head = self._head._next
            return n
        return None

    # define this
    def add_to_end(self, new):
        current = self._head
        if current == None:
            self._head = new
        else:
            while current._next != None:
                current = current._next
            current._next = new

    def __str__(self):
        string = 'LList -> '
        current = self._head
        while current != None:
            string += str(current)
            current = current._next
        return string


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def __str__(self):
        if self._next == None:
            nxt = "None"
        else:
            nxt = "->"
        return " |" + str(self._value) + "|:" + nxt


def main():
    # 1. make a linked list with three elements
    list = LinkedList()
    list.add(Node(1))
    list.add(Node(2))
    list.add(Node(3))

    # use the method print_elements() to print out the elements
    list.print_elements()

    # use print() to print the linked list
    print(list)

    # 2. define incr() and call it
    list.incr()

    # 3. define linkedlist_to_plist() and call it
    print(list.linkedlist_to_plist())

    # 4. define remove_first() and call it
    print(list.remove_first())
    print(list)

    # make sure to test all list sizes 
    # an empty list and a list of one element
    print("more tests for remove_first()")
    list = LinkedList()
    print(list.remove_first())
    list.add(Node(1))
    print(list.remove_first())
    print(list)

    # 5. define add_to_end()  see slides 114 or 115
    # make a node n and add it to the end of the linked list
    # print the linked list
    n = Node(4)
    list.add_to_end(n)
    print(list)


main()
