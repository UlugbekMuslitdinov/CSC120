"""
    File: writer_bot_ht.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: This program generates a text by analyzing a text file
"""

import sys
import random

SEED = 8   # SEED for random number generator
random.seed(SEED)

file = input() # file name
m = input() # hashtable size
n = int(input()) # prefix size
number_of_words = int(input()) # number of words to generate

if int(n) < 1:
    print("ERROR: specified prefix size is less than one")
    sys.exit(0)
if int(number_of_words) < 1:
    print("ERROR: specified size of the generated text is less than one")
    sys.exit(0)


class HashTable:
    """
    This class is a hash table that stores prefixes as keys and the list of suffixes as values.

    Attributes:
        _size (int): The size of the hash table
        _pairs (list): The list of pairs (prefix, suffixes)

    Methods:
        put(key, value): Adds a new pair to the hash table
        get(key): Returns the value of the given key
        __contains__(key): Returns True if the key is in the hash table
        __str__(): Returns the string representation of the hash table
    """
    def __init__(self, size):
        self._size = size
        self._pairs = [None] * size

    def put(self, key, value):
        """
        Adds a new pair to the hash table

        Args:
            key (tuple): The prefix
            value (list): The list of suffixes

        Returns:
            None
        """
        if self.get_index(key) is None:
            if not self.next_empty() is None:
                self._pairs[self.next_empty()] = (key, [value])
        else:
            self._pairs[self.get_index(key)][1].append(value)

    def next_empty(self):
        """
        Returns the index of the next empty bucket in the hash table

        Args:
            None

        Returns:
            int: The index of the next empty bucket in the hash table
        """
        for i in range(len(self._pairs)):
            if self._pairs[i] is None:
                return i
        return None

    def get(self, key):
        """
        Returns the value of the given key

        Args:
            key (tuple): The prefix

        Returns:
            list: The list of suffixes
        """
        for pair in self._pairs:
            if pair is not None:
                if pair[0] == key:
                    return pair[1]
        return None

    def get_index(self, key):
        """
        Returns the index of the given key

        Args:
            key (tuple): The prefix

        Returns:
            int: The index of the given key
        """
        for i in range(len(self._pairs)):
            if self._pairs[i] is not None:
                if self._pairs[i][0] == key:
                    return i
                if self._pairs[i] is None:
                    return None
        return None

    def __contains__(self, key):
        """
        Returns True if the key is in the hash table

        Args:
            key (tuple): The prefix

        Returns:
            bool: True if the key is in the hash table
        """
        for pair in self._pairs:
            if pair[0] == key:
                return True
        return False

    def __str__(self):
        return str(self._pairs)


# Read the file and store the words in a list
all_words = []
stripped_words = []
file_content = open(file, "r").read().splitlines()
for line in file_content:
    for word in line.split():
        all_words.append(word)
        stripped_words.append(word)


data = HashTable(int(m))
for i in range(len(all_words) - n + 1):
    prefix = tuple(stripped_words[i:i+n])
    if i+n < len(all_words):
        suffix = all_words[i+n]
    else:
        suffix = ""
    data.put(prefix, suffix)

# Generate the text
prefix = tuple(stripped_words[0:n])
new_text = stripped_words[0:n]
while len(new_text) < number_of_words:
    if data.get(prefix) is None:
        break
    if len(data.get(prefix)) == 1:
        new_text.append(data.get(prefix)[0])
    else:
        new_text.append(data.get(prefix)[random.randint(0, len(data.get(prefix))-1)])
    prefix = prefix[1:] + (new_text[-1],)

# Print 10 words per line
for i in range(len(new_text)):
    if i % 10 == 0:
        print()
    print(new_text[i], end=" ")