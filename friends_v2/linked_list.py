class Node:
    def __init__(self, name):
        self.name = name
        self.included_nodes = LinkedList()
        self.next = None

    def add_node(self, node):
        self.included_nodes.add_to_head(node)

    def get_nodes_list(self):
        return_list = []
        current = self.included_nodes.get_head()
        while current is not None:
            return_list.append(current.name)
            current = current.get_next()
        return return_list

    def __str__(self):
        return str(self.name)

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_name(self):
        return self.name


class LinkedList:

    def __init__(self):
        self._head = None

    def add_to_head(self, value):
        if self._head is None:
            self._head = value
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = value

    def remove_from_head(self):
        self._head = self._head.next

    def get_head(self):
        return self._head

    def __str__(self):
        current = self._head
        return_string = ""
        while current is not None:
            return_string += str(current) + " "
            current = current.next
        return return_string

    def get_nodes(self):
        current = self._head
        nodes = []
        while current is not None:
            nodes.append(current)
            current = current.next
        return nodes
