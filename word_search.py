"""
    File: word_search.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Finds words in a word search puzzle.
"""


def extract_strings_from_grid(grid):
    """
        Return a slist of strings from the grid that can occur horizontally, vertically or diagonal.

        Args:
            grid (list): A slist of strings that represent the grid.

        Returns:
            list: A slist of strings that occur in the grid vertically, horizontally or by diagonal.

        Pre-condition:
            grid is a slist of strings.

        Post-condition:
            A slist of strings that occur in the grid vertically, horizontally or by diagonal is returned.
    """
    horizontal_left_to_right = []
    for row in grid:
        words = "".join(row.split())
        horizontal_left_to_right.append(words)
    horizontal_right_to_left = []
    for row in grid:
        words = "".join(row.split())
        horizontal_right_to_left.append(words[::-1])
    vertical_top_to_bottom = []
    for i in range(len(grid[0])):
        words = "".join([row[i] for row in grid])
        vertical_top_to_bottom.append(words)
    vertical_bottom_to_top = []
    for i in range(len(grid[0])):
        words = "".join([row[i] for row in grid])
        vertical_bottom_to_top.append(words[::-1])

    diagonals = []
    letter_sets = [i.split() for i in grid]
    i = len(letter_sets)
    max_horizontal = len(letter_sets) - 1
    max_vertical = len(letter_sets) - 1
    horizontal_start = 0
    while i >= 0:
        horizontal_now = horizontal_start
        vertical_now = 0
        str_now = ""
        while horizontal_now <= max_horizontal and vertical_now <= max_vertical:
            str_now += letter_sets[horizontal_now][vertical_now]
            vertical_now += 1
            horizontal_now += 1
        horizontal_start += 1
        diagonals.append(str_now)
        i -= 1
    i = len(letter_sets) - 1
    vertical_start = 1
    while i >= 0:
        horizontal_now = 0
        vertical_now = vertical_start
        str_now = ""
        while horizontal_now <= max_horizontal and vertical_now <= max_vertical:
            str_now += letter_sets[horizontal_now][vertical_now]
            vertical_now += 1
            horizontal_now += 1
        vertical_start += 1
        diagonals.append(str_now)
        i -= 1
    for i in range(len(diagonals) - 1):
        if diagonals[i] == "":
            diagonals.pop(i)
    all_strings = (
        horizontal_left_to_right
        + horizontal_right_to_left
        + vertical_top_to_bottom
        + vertical_bottom_to_top
        + diagonals
    )
    return all_strings


def word_search(grid, word_list):
    """
        Return a slist of words that occur in the grid found in the wordlist.

        Args:
            grid (str): A string that represents the name of file of the grid.
            word_list (str): A string that represents the name of file of word slist.

        Returns:
            list: A slist of words that occur in the grid found in the wordlist.

        Pre-condition:
            grid is a string that represents the name of file of the grid.
            word_list is a string that represents the name of file of word slist.

        Post-condition:
            A slist of words that occur in the grid found in the wordlist is returned.
    """
    grid_strings = open(grid).read().splitlines()
    extracted_strings = extract_strings_from_grid(grid_strings)
    word_list = open(word_list).read().splitlines()
    word_occured = []
    for word in word_list:
        for string in extracted_strings:
            if word in string.lower() and len(word) > 2:
                word_occured.append(word)
                break
    return word_occured


def main():
    """
        Main function. Prints the words that occur in the grid found in the wordlist.

        Args:
            None.

        Returns:
            None.
    """
    word_list_file = input()
    grid_file = input()
    words = word_search(grid_file, word_list_file)
    for word in sorted(words):
        print(word)


main()
