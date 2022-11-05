"""
    File: huffman.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Encode and decode the string using the Huffman tree.
"""


class BinaryTree:
    """
    This class is used to create the Binary Tree.

    Attributes:
        value (str): The value of the node.
        left (BinaryTree): The left child of the node.
        right (BinaryTree): The right child of the node.

    Methods:
        __str__(): Returns the string representation of the BinaryTree object.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}, ({self.left}, {self.right})"


def create_tree(pre_order, in_order):
    """
    This function is used to create the Binary Tree using the pre-order and in-order traversal.

    Parameters:
        pre_order (list): The list of values in the pre-order traversal.
        in_order (list): The list of values in the in-order traversal.

    Returns:
        BinaryTree: The Binary Tree.

    Pre-condition:
        The pre-order and in-order traversal must be valid.

    Post-condition:
        The Binary Tree is created.
    """
    if len(pre_order) == 0:
        return None
    else:
        root = BinaryTree(pre_order[0])
        root_index = in_order.index(pre_order[0])
        root.left = create_tree(pre_order[1:root_index + 1], in_order[:root_index])
        root.right = create_tree(pre_order[root_index + 1:], in_order[root_index + 1:])
        return root


def decode(tree, encoder):
    """
    This function is used to decode the string using the Huffman tree.

    Parameters:
        tree (BinaryTree): The Huffman tree.
        encoder (str): The string to be decoded.

    Returns:
        str: The decoded string.

    Pre-condition:
        The Huffman tree must be valid.
        Encoder must be non-empty.

    Post-condition:
        The string is decoded.
    """
    if len(encoder) == 0:
        return ""
    else:
        return_str = ""
        node = tree
        index = 0
        while index < len(encoder):
            if encoder[index] == "0":
                node = node.left
            else:
                node = node.right
            if node is None:
                return ""
            if index+1<len(encoder):
                if encoder[index+1] == "0" and node.left is None or encoder[index+1] == "1" and node.right is None:
                    return_str += str(node.value)
                    node = tree
            if node.left is None and node.right is None:
                return_str += str(node.value)
                node = tree
            index += 1
        return return_str


def postorder(tree):
    """
    This function is used to print the post-order traversal of the tree.

    Parameters:
        tree (BinaryTree): The tree.

    Returns:
        str: The post-order traversal of the tree.

    Pre-condition:
        The tree must be valid.

    Post-condition:
        The post-order traversal is printed.
    """
    if tree is None:
        return ""
    else:
        return postorder(tree.left) + postorder(tree.right) + str(tree.value) + " "


def main():
    """
    This function is used to get the input and call the functions to create the tree and decode the string.

    Parameters:
        None

    Returns:
        None
    """
    fname = str(input('Input file: '))
    file = open(fname, 'r').read().splitlines()
    pre_order = file[0].split()
    in_order = file[1].split()
    encoder = file[2]
    tree = create_tree(pre_order, in_order)
    print(postorder(tree))
    print(decode(tree, encoder))


# Call the main function
main()
