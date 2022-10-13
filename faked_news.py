class Node:
    def __init__(self, word):
        self._word = word
        self._count = 0
        self._next = None

    def word(self):
        return self._word

    def count(self):
        return self._count

    def next(self):
        return self._next

    def set_next(self, target):
        self._next = target

    def increment(self):
        self._count += 1

    def __str__(self):
        return f"{self._word} {self._count}"

    def __repr__(self):
        return f"{self._word} {self._count}"


class LinkedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def head(self):
        return self._head

    def update_count(self, word):
        current = self._head
        while current is not None:
            if current.word() == word:
                current.increment()
                return
            current = current.next()
        self.add(word)

    def add(self, word):
        new_node = Node(word)
        new_node.set_next(self._head)
        self._head = new_node

    def rm_from_hd(self):
        if self._head is None:
            return
        self._head = self._head.next()

    def insert_after(self, node1, node2):
        node2.set_next(node1.next())
        node1.set_next(node2)

    def sort(self):
        # Sort the linked list in descending order by count
        if self._head is None:
            return
        current = self._head
        to_be_sorted = self
        sorted = LinkedList()
        sorted.add(current)
        to_be_sorted.rm_from_hd()
        while to_be_sorted._head is not None:
            current = to_be_sorted._head
            to_be_sorted.rm_from_hd()
            if current.count() > sorted.head().count():
                sorted.insert_after(sorted.head(), current)
            else:
                sorted.add(current)
        self = sorted

    def get_nth_highest_count(self, n):
        # Return the nth highest count in the linked list
        current = self._head
        for i in range(n):
            current = current.next()
        return current.count()