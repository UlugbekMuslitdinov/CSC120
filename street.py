"""
    File: street.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: This program takes a string input from the user and prints a street map
"""


def print_building(width, height, brick, current_height):
    """
    This function prints a building with given width, height, and brick

    Parameters:
        width (int): width of the building
        height (int): height of the building
        brick (str): brick of the building
        current_height (int): current height of the building

    Returns:
        str: a string of the building

    Pre-conditions:
        width > 0
        height > 0
        brick is a single character
        current_height > 0

    Post-conditions:
        returns a string of the building
    """
    if height >= current_height > 0:
        return brick * width
    elif current_height > height:
        return " " * width
    else:
        return width * " "


def print_park(width, block, current_height):
    """
    This function prints a park with given width, height, and brick

    Parameters:
        width (int): width of the park
        block (str): block of the park
        current_height (int): current height of the park

    Returns:
        str: a string of the park

    Pre-conditions:
        width > 0
        block is a single character
        current_height > 0

    Post-conditions:
        returns a string of the park
    """
    if current_height > 5:
        return " " * width
    elif current_height == 5:
        return width//2 * " " + block + width//2 * " "
    elif current_height == 4:
        return ((width//2)-1) * " " + block*3 + ((width//2)-1) * " "
    elif current_height == 3:
        return ((width//2)-2) * " " + block*5 + ((width//2)-2) * " "
    elif current_height == 2 or current_height == 1:
        return width//2 * " " + "|" + width//2 * " "


def print_empty_lot(width, block, current_height):
    """
    This function prints an empty lot with given width, height, and brick

    Parameters:
        width (int): width of the empty lot
        block (str): block of the empty lot
        current_height (int): current height of the empty lot

    Returns:
        str: a string of the empty lot

    Pre-conditions:
        width > 0
        current_height > 0

    Post-conditions:
        returns a string of the empty lot
    """
    if current_height == 1:
        return str(width*block.replace("_", " "))[:width]
    else:
        return width*" "


def print_line(obj, current_height, string_to_append):
    """
    This function prints a line of the street map

    Parameters:
        obj (list): list of objects
        current_height (int): current height of the street map
        string_to_append (str): string to append to the end of the line

    Returns:
        str: a string of the line

    Pre-conditions:
        obj is a list
        current_height > 0
        string_to_append is a string

    Post-conditions:
        returns a string of the line
    """
    result_line = string_to_append
    if len(obj) == 0:
        return result_line
    else:
        current_object = obj[0]
        params = current_object.split(":")[1].split(",")
        if current_object[0] == "b":
            result_line += print_building(int(params[0]), int(params[1]), params[2], current_height)
        elif current_object[0] == "p":
            result_line += print_park(int(params[0]), params[1], current_height)
        elif current_object[0] == "e":
            result_line += print_empty_lot(int(params[0]), params[1], current_height)
        return print_line(obj[1:], current_height, result_line)


def sum_width(obj):
    """
    This function sums the width of the objects

    Parameters:
        obj (list): list of objects

    Returns:
        int: sum of the width of the objects

    Pre-conditions:
        obj is a list

    Post-conditions:
        returns sum of the width of the objects
    """
    if len(obj) == 0:
        return 0
    else:
        current_object = obj[0].split(":")
        params = current_object[1].split(",")
        if current_object[0] == "b":
            return int(params[0]) + sum_width(obj[1:])
        elif current_object[0] == "p":
            return int(params[0]) + sum_width(obj[1:])
        elif current_object[0] == "e":
            return int(params[0]) + sum_width(obj[1:])


def max_height(obj):
    """
    This function finds the maximum height of the building

    Parameters:
        obj (list): list of objects

    Returns:
        int: maximum height of the building

    Pre-conditions:
        obj is a list

    Post-conditions:
        returns maximum height of the building
    """
    if len(obj) == 0:
        return 0
    else:
        current_object = obj[0].split(":")
        params = current_object[1].split(",")
        if current_object[0] == "b":
            return max(int(params[1]), max_height(obj[1:]))
        else:
            return max_height(obj[1:])


def has_park(obj):
    """
    This function checks if the street map has a park

    Parameters:
        obj (list): list of objects

    Returns:
        bool: True if the street map has a park, False otherwise

    Pre-conditions:
        obj is a list

    Post-conditions:
        returns True if the street map has a park, False otherwise
    """
    if len(obj) == 0:
        return False
    else:
        current_object = obj[0].split(":")
        if current_object[0] == "p":
            return True
        else:
            return has_park(obj[1:])


def has_building(obj):
    """
    This function checks if the street map has a building

    Parameters:
        obj (list): list of objects

    Returns:
        bool: True if the street map has a building, False otherwise

    Pre-conditions:
        obj is a list

    Post-conditions:
        returns True if the street map has a building, False otherwise
    """
    if len(obj) == 0:
        return False
    else:
        current_object = obj[0].split(":")
        if current_object[0] == "b":
            return True
        else:
            return has_building(obj[1:])


def has_empty_lot(obj):
    """
    This function checks if the street map has an empty lot

    Parameters:
        obj (list): list of objects

    Returns:
        bool: True if the street map has an empty lot, False otherwise

    Pre-conditions:
        obj is a list

    Post-conditions:
        returns True if the street map has an empty lot, False otherwise
    """
    if len(obj) == 0:
        return False
    else:
        current_object = obj[0].split(":")
        if current_object[0] == "e":
            return True
        else:
            return has_empty_lot(obj[1:])


def print_whole_map(obj, current_height):
    """
    This function prints the whole street map

    Parameters:
        obj (list): list of objects
        current_height (int): current height of the street map

    Returns:
        str: a string of the street map

    Pre-conditions:
        obj is a list

    Post-conditions:
        returns a string of the street map
    """
    if current_height == 0:
        return
    else:
        print(print_line(obj, current_height, "|") + "|")
        print_whole_map(obj, current_height-1)


def main():
    """
    This function is the main function of the program
    Gets the input from the user and prints the street map

    Parameters:
        None

    Returns:
        None
    """
    user_pattern = str(input("Street: "))
    objects = user_pattern.split()
    street_width = sum_width(objects)
    street_height = max_height(objects) + 1
    if street_height < 6 and has_park(objects):
        street_height = 6
    elif street_height < 2 and has_empty_lot(objects):
        street_height = 2
    else:
        street_height = street_height
    upper_lower_border = "+" + street_width * "-" + "+"
    print(upper_lower_border)
    print_whole_map(objects, street_height)
    print(upper_lower_border)


main()
