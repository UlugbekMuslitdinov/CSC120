"""
    File: fake_news.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: This program reads a csv file and counts the number of
        times each word appears in the title column
        and prints the top n words in descending order of frequency.
"""


import csv


class Node:
    """
    This class represents a node in a linked list. Each node contains a
    word and a count of how many times that word appears in the title
    column of the csv file. The node also contains a pointer
    to the next node in the list.

    Attributes:
        word (str): The word that the node contains
        count (int): The number of times the word appears
            in the title column of the csv file
        next (Node): The next node in the linked list

    Methods:
        word(): Returns the word that the node contains
        count(): Returns the number of times the word appears
            in the title column of the csv file
        next(): Returns the next node in the linked list
        set_next(target): Sets the next node in the linked list to target
        increment(): Increments the count of the word by 1
        __str__(): Returns a string representation of the node
        __repr__(): Returns a string representation of the node
    """
    def __init__(self, word):
        self._word = word
        self._count = 1
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
        return f"{self._word} : {self._count}"

    def __repr__(self):
        return f"{self._word} {self._count}"


class LinkedList:
    """
    This class represents a linked list. Each node in the
    linked list contains a word and a count of how many times
    that word appears in the title column of the csv file.
    The linked list can be sorted in descending order by count.

    Attributes:
        head (Node): The initial Node the linked list

    Methods:
        is_empty(): Returns True if the linked list is
            empty, False otherwise
        head(): Returns the head of the linked list
        update_count(word): Updates the count of the
            word in the linked list by 1
        add(word): Adds a new node to the linked
            list with the word and count of 1
        rm_from_hd(): Removes the head of the linked list
        insert_after(node1, node2): Inserts node2 after node1
        sort(): Sorts the linked list in descending order by count
        get_nth_highest_count(n): Returns the nth highest
            count in the linked list
        print_upto_count(n): Prints all words that have
            the count at least n
        __str__(): Returns a string representation of the linked list
        __repr__(): Returns a string representation of the linked list
    """

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def head(self):
        return self._head

    def update_count(self, word):
        # Update the count of the word in the linked list by 1
        # If the word is not in the linked list, add it to the linked list
        current = self._head
        while current is not None:
            if current.word() == word:
                current.increment()
                return
            current = current.next()
        self.add(word)

    def add(self, word):
        # Add a new node to the linked list with the word and count of 1
        new_node = Node(word)
        new_node.set_next(self._head)
        self._head = new_node

    def rm_from_hd(self):
        # Remove the head of the linked list
        if self._head is None:
            return
        self._head = self._head.next()

    def insert_after(self, node1, node2):
        node2.set_next(node1.next())
        node1.set_next(node2)

    def sort(self):
        # Sort the linked list in descending order by count
        current = self._head
        sorted_list = [current]
        current = current.next()
        while current is not None:
            for i in range(len(sorted_list)):
                if current.count() > sorted_list[i].count():
                    sorted_list.insert(i, current)
                    break
            else:
                sorted_list.append(current)
            current = current.next()
        self._head = sorted_list[0]
        for i in range(len(sorted_list) - 1):
            sorted_list[i].set_next(sorted_list[i + 1])
        sorted_list[-1].set_next(None)

    def get_nth_highest_count(self, n):
        # Return the nth highest count in the linked list
        current = self._head
        for i in range(n):
            current = current.next()
        return current.count()

    def print_upto_count(self, n):
        # Print all words that have the count at least n
        current = self._head
        till_count = self.get_nth_highest_count(n)
        while current is not None:
            if current.count() >= till_count:
                print(current)
            if current.count() < till_count:
                break
            current = current.next()

    def __str__(self):
        current = self._head
        result = ""
        while current is not None:
            result += str(current) + "->"
            current = current.next()
        return result

    def __repr__(self):
        current = self._head
        result = ""
        while current is not None:
            result += str(current) + "->"
            current = current.next()
        return result


def remove_punctuation(row):
    """
    This function removes all punctuation from the row and
        returns the row with space in place of punctuation.

    Parameters:
        row (str): The row that needs to be cleaned

    Returns:
        row (str): The row with space in place of punctuation

    Pre-condition:
        row is a string

    Post-condition:
        row is a string with space in place of punctuation
    """
    punctuation = ".,!?\"\'[]:;(){}#-"
    result_row = ""
    for char in row:
        if char in punctuation:
            result_row += " "
        else:
            result_row += char
    return result_row


def main():
    # Read the csv file
    data_list = LinkedList()
    filename = input()
    f = open(filename, "r")
    f = csv.reader(f)
    # loop through the csv file
    for row in f:
        # remove punctuation from the row
        title = row[4]
        title = remove_punctuation(title)
        title = title.split()
        for word in title:
            # update the count of the word in the linked list by 1
            word = word.lower().strip(".,!?\"\'[]:;(){}#")
            if "'" in word:
                word = word.split("'")
                for w in word:
                    if len(w) > 2:
                        data_list.update_count(w)
            elif len(word) > 2:
                data_list.update_count(word)
    # sort the linked list in descending order by count
    data_list.sort()
    n = int(input())
    data_list.print_upto_count(n)


main()
