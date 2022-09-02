def occurs_in(substr, word_list):
    """Return a list of words that occur in the word search."""
    return [word for word in word_list if substr in word]


def extract_strings_from_grid(grid):
    """Return a list of strings from the grid that can occur horizontally, vertically or diagonal."""
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
    diagonal_top_left_to_bottom_right = []
    i = 0
    while i < len(grid):
        string = ""
        horizontal_coursor = 0
        vertical_coursor = 0
        while horizontal_coursor < len(grid) and vertical_coursor < len(grid):
            string += grid[horizontal_coursor][vertical_coursor]
            horizontal_coursor += 1
            vertical_coursor += 1
        diagonal_top_left_to_bottom_right.append(string)
        i += 1
        horizontal_coursor += 1
    i = 0
    while i < len(grid):
        string = ""
        horizontal_coursor = 0
        vertical_coursor = 0
        while horizontal_coursor < len(grid) and vertical_coursor < len(grid):
            string += grid[horizontal_coursor][vertical_coursor]
            horizontal_coursor += 1
            vertical_coursor += 1
        diagonal_top_left_to_bottom_right.append(string)
        i += 1
        vertical_coursor += 1
    all_strings = horizontal_left_to_right + horizontal_right_to_left + vertical_top_to_bottom + vertical_bottom_to_top + diagonal_top_left_to_bottom_right
    return all_strings


def word_search(grid, word_list):
    """Return a list of words that occur in the word search."""
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
    """Main function."""
    word_list_file = input()
    grid_file = input()
    print(word_search(grid_file, word_list_file))


main()
