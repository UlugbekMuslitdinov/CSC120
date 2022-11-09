class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class ADT:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def is_empty(self):
        return self.head is None


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)


def get_height(root):
    if root is None:
        return 0
    else:
        return 1 + max(get_height(root.left), get_height(root.right))


def print_node(node, indent):
    if node is None:
        return
    print(f"->{indent*4*' '}{node.value}")
    print_node(node.left, indent+1)
    print_node(node.right, indent+1)


def print_tree(root):
    """
    Print tree with indentation, where each level is indented 4 spaces.
    """
    if root is None:
        return
    print(f"-> {root.value}")
    print_node(root.left, 1)
    print_node(root.right, 1)


tree = BinaryTree(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
print_tree(tree)
