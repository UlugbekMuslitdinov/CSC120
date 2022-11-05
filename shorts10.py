class BinaryTree:
    def __init__(self,value):
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
        if self._right == None:
            self._right = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._right = self._right
            self._right = t

    def insert_left(self, value):
        if self._left == None:
            self._left = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._left = self._left
            self._left = t


def tree_count(tree):
    if tree is None:
        return 0
    if tree._right is not None and tree._left is not None:
        return 1 + tree_count(tree._left) + tree_count(tree._right)
    elif tree._right is not None:
        return 1 + tree_count(tree._right)
    elif tree._left is not None:
        return 1 + tree_count(tree._left)
    else:
        return 1


def tree_sum(tree):
    if tree is None:
        return 0
    if tree._right is not None and tree._left is not None:
        return tree._value + tree_sum(tree._left) + tree_sum(tree._right)
    elif tree._right is not None:
        return tree._value + tree_sum(tree._right)
    elif tree._left is not None:
        return tree._value + tree_sum(tree._left)
    else:
        return tree._value


def tree_height(tree):
    if tree is None:
        return 0
    if tree._right is not None and tree._left is not None:
        return max(tree_height(tree._left), tree_height(tree._right))
    elif tree._right is not None:
        return 1 + tree_height(tree._right)
    elif tree._left is not None:
        return 1 + tree_height(tree._left)
    else:
        return 1


def count_interior(tree):
    if tree is None:
        return 0
    if tree._right is not None and tree._left is not None:
        return 1 + count_interior(tree._left) + count_interior(tree._right)
    elif tree._right is not None:
        return 1 + count_interior(tree._right)
    elif tree._left is not None:
        return 1 + count_interior(tree._left)
    else:
        return 0