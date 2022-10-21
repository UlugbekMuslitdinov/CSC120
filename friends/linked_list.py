"""
    File: linked_list.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Create the LinkedList object and the Friend object.
"""


class Friend:
    """
    This class is used to create the Friend object.

    Attributes:
        value (str): The name of the friend.
        friends (LinkedList): The list of friends of the friend.
        next (Friend): The next friend in the list.

    Methods:
        add_friend(self, friend): Adds the friend to the list of friends of the friend.
        get_friends(self): Returns the list of friends of the friend.
        __str__(self): Returns the name of the friend.
        set_next(self, node): Sets the next friend in the list.
        get_next(self): Returns the next friend in the list.
        get_value(self): Returns the name of the friend.
    """
    def __init__(self, name):
        self.value = name
        self.friends = LinkedList()
        self.next = None

    def add_friend(self, friend):
        self.friends.add(friend)

    def get_friends(self):
        """
        Returns the list of friends of the friend.

        Args:
            self (Friend): An instance of Friend.

        Returns:
            LinkedList: The list of friends of the friend.
        """
        current = self.friends._head
        friends = []
        while current is not None:
            friends.append(current.value)
            current = current.next
        return sorted(friends)

    def __str__(self):
        return str(self.value)

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value


class LinkedList:
    """
    This class is used to create the LinkedList object to store the list of friends of the friend.

    Attributes:
        _head (Friend): The first friend in the list.

    Methods:
        add(self, value): Adds the friend to the list.
        __str__(self): Returns the list of friends of the friend.
        __iter__(self): Returns the iterator.
        remove(self): Removes the first friend in the list.
    """

    def __init__(self):
        self._head = None

    def add(self, value):
        """
        Adds the friend to the list.

        Args:
            value (Friend): The friend to add to the list.

        Returns:
            None
        """
        if self._head is None:
            self._head = value
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = value

    def __str__(self):
        current = self._head
        while current is not None:
            print(current.get_friends())
            current = current.next
        return ""

    def __iter__(self):
        self._current = self._head
        return self

    def remove(self):
        """
        Removes the first friend in the list.

        Args:
            None

        Returns:
            None
        """
        self._head = self._head.next
