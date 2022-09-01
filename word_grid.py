import random

letters = "abcdefghijklmnopqrstuvwxyz"


def init():
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size


def make_grid(grid_size):
    grid = []
    for i in range(grid_size):
        grid.append([])
        for j in range(grid_size):
            grid[i].append(random.choice(letters))
    return grid


def print_grid(grid):
    for i in range(len(grid)):
        row = []
        for j in range(len(grid)):
            row.append(grid[i][j])
        print(",".join(row))
        print()


def main():
    grid_size = init()
    grid = make_grid(grid_size)
    print_grid(grid)


main()
