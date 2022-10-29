# Sitcom

class BinaryTree:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def value(self):
        return self._value

    def left(self):
        return self._left

    def right(self):
        return self._right

    def insert_right(self, value):
        if self._right is None:
            self._right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node._right = self._right
            self._right = new_node

    def insert_left(self, value):
        if self._left is None:
            self._left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node._left = self._left
            self._left = new_node

