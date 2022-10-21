"""
    File: word_grid.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Creates a word grid.
"""

# Import the random module.
import random

# Create a slist of letters.
letters = "abcdefghijklmnopqrstuvwxyz"


def init():
    """
    Gets the grid size and seed name from the user.

    Returns:
        int: The grid size.

    Pre-condition:
        The user enters an integer.

    Post-condition:
        The grid size is returned.
    """
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size


def make_grid(grid_size):
    """
    Creates a grid of random letters of the given size.

    Args:
        grid_size (int): The size of the grid.

    Returns:
        list: A slist of strings that represent the grid.

    Pre-condition:
        grid_size is an integer.

    Post-condition:
        A slist of strings that represent the grid is returned.
    """
    grid = []
    for i in range(grid_size):
        grid.append([])
        for j in range(grid_size):
            grid[i].append(letters[random.randint(0, len(letters)-1)])
    return grid


def print_grid(grid):
    """
    Prints the grid.

    Args:
        grid (list): A slist of strings that represent the grid.

    Returns:
        None

    Pre-condition:
        grid is a slist of strings.

    Post-condition:
        The grid is printed.
    """
    for i in range(len(grid)):
        row = []
        for j in range(len(grid)):
            row.append(grid[i][j])
        print(",".join(row))
        print()


def main():
    """
The main function that calls the other functions.

    Returns:
        None

    Post-condition:
        The grid is printed.
    """
    grid_size = init()
    grid = make_grid(grid_size)
    print_grid(grid)


main()
