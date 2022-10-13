# STAR
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value


class LinkedList:
    def __init__(self):
        self._head = None

    def add(self, new):
        new._next = self._head
        self._head = new

    def remove(self):
        if self._head is None:
            return None
        node = self._head
        self._head = node._next
        node._next = None
        return node

    def is_empty(self):
        return self._head is None


class Stack:
    def __init__(self):
        self._items = LinkedList()

    def push(self, new):
        self._items.add(new)

    def pop(self):
        return self._items.remove()

    def is_empty(self):
        return self._items.is_empty()

    def __str__(self):
        return str(self._items)


class Queue:
    def __init__(self):
        self._items = LinkedList()

    def enqueue(self, new):
        self._items.add(new)

    def dequeue(self):
        return self._items.remove()
