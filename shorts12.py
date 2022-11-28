def preorder_to_bst(preorder):
    if not preorder:
        return "None"
    root = preorder[0]
    left = []
    right = []
    for i in range(1, len(preorder)):
        if preorder[i] < root:
            left.append(preorder[i])
        else:
            right.append(preorder[i])
    left_tree = str(preorder_to_bst(left))
    right_tree = str(preorder_to_bst(right))
    if not left:
        left_tree = "None"
    if not right:
        right_tree = "None"
    return "(" + str(root) + " " + left_tree + " " + right_tree + ")"


# <============================================================================================>
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    # your code goes here
    def remove_last(self):
        if self._head == None:
            return
        current = self._head
        while current._next != self._tail:
            current = current._next
        self._tail = current
        current._next = None

    def add(self, new):
        new._next = self._head
        # if the list is empty, both
        # the head and tail will reference
        # this new node
        if self._head == None:
            self._tail = new
        self._head = new

    def __str__(self):
        string = 'LList -> '
        current = self._head
        while current != None:
            string += str(current)
            current = current._next
        return string + '; tail -> ' + str(self._tail)


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


# <============================================================================================>

def str2objects(spec):
    specs = spec.split()
    objects = []
    for s in specs:
        if s == "dict":
            objects.append({})
        elif s == "list":
            objects.append([])
        elif s == "set":
            objects.append(set())
        elif s == "tuple":
            objects.append(())
        elif s == "str":
            objects.append("")
    return objects


# <============================================================================================>

class Queue:
    def __init__(self):
        self.obj = ""

    def enqueue(self, item):
        self.obj += item

    def dequeue(self):
        removed = self.obj[0]
        self.obj = self.obj[1:]
        return removed

    def is_empty(self):
        return self.obj == ""

    def __str__(self):
        return self.obj


q = Queue()
for c in "abcd":
    q.enqueue(c)
q.dequeue()
print(q.dequeue())
