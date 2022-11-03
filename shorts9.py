def list_to_string(list):
    """
    Convert a list to a string with {} in between each element.

    Arguments:
        list: a list of strings

    Returns:
        a string containing the elements of the list

    Pre-conditions:
        list must contain strings

    Post-conditions:
        the returned string must contain the elements of the list
    """
    if len(list) == 1:
        return str(list[0])
    else:
        return str(list[0]) + '{}' + list_to_string(list[1:])


def fmt(spec, values):
    """
    Format a spec according to the value.

    Arguments:
        spec: a string containing a format specifier
        values: a value to be formatted

    Returns:
        a string containing the formatted value

    Pre-conditions:
        spec must contain a string
        value must be a string, integer, or float

    Post-conditions:
        the returned string must contain the formatted value
    """
    split_text = spec.split('{}')
    if len(split_text) == 1:
        return split_text[0]
    else:
        return split_text[0] + str(values[0]) + fmt(list_to_string(split_text[1:]), values[1:])


# <==================================== TASK 2 ================================================>
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def add(self, value):
        if self.root is None:
            self.root = value
        else:
            if value < self.root:
                if self.left is None:
                    self.left = BinarySearchTree()
                self.left.add(value)
            else:
                if self.right is None:
                    self.right = BinarySearchTree()
                self.right.add(value)

    def find(self, value):
        if self.root == value:
            return self
        elif self.root > value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(value)

    def __str__(self):
        return "({:d} {} {})".format(self.root, str(self.left), str(self.right))