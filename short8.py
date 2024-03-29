def list2string(arglist):
    """
    Convert a list of strings to a single string

    Args:
        arglist (list): The list of strings to convert

    Returns:
        str: The single string
    """
    if len(arglist) == 0:
        return ""
    elif len(arglist) == 1:
        return arglist[0]
    else:
        return arglist[0] + list2string(arglist[1:])


def palindrome_list(arglist):
    """
    Check if a list of strings is a palindrome

    Args:
        arglist (list): The list of strings to check

    Returns:
        bool: True if the list is a palindrome, False otherwise
    """
    if len(arglist) == 0:
        return True
    elif len(arglist) == 1:
        return True
    elif len(arglist) == 2:
        return arglist[0] == arglist[1]
    else:
        return arglist[0] == arglist[-1] and palindrome_list(arglist[1:-1])


def column2list_rec(grid, n):
    """
    Convert a column of a grid to a list

    Args:
        grid (list): The grid to convert
        n (int): The column number

    Returns:
        list: The list of strings
    """
    if len(grid) == 0:
        return []
    else:
        return [grid[0][n]] + column2list_rec(grid[1:], n)


def diag2list_rec(grid):
    """
    Convert a diagonal of a grid to a list

    Args:
        grid (list): The grid to convert

    Returns:
        list: The list of strings
    """
    if len(grid) == 1 and type(grid[0]) != "list" or len(grid) == 0:
        return []
    else:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if grid[len(grid) - 1] in nums:
            index = int(grid.pop(len(grid) - 1))
            new_grid = grid[1:]
            return [grid[0][index]] + diag2list_rec(new_grid + [index + 1])
        else:
            new_grid = grid[1:]
            return [grid[0][0]] + diag2list_rec(new_grid + [1])


print(diag2list_rec([[1]]))