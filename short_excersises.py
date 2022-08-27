def number2letter(n):
    """
    Convert a number to a letter.

    Parameters: n (int) from 0 to 25

    Returns: the letter (char) corresponding to n
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters[n]


def concat_elements(slist, startpos, stoppos):
    """
    Concatenate elements of a list.

    Parameters: slist (list)
                startpos (int)
                stoppos (int)
    Returns: the concatenated string
    """
    # If no arguments are given, return None
    if not slist or not startpos or not stoppos:
        return None
    if stoppos < startpos:
        return ""   # Return empty string if startpos is greater than stoppos
    if startpos < 0:
        startpos = 0    # Set startpos to 0 if it is less than 0
    if stoppos > len(slist):
        stoppos = len(slist)    # Set stoppos to the length of the list if it is greater than the length of the list
    return_string = ""
    while startpos <= stoppos:
        return_string += slist[startpos]
        startpos += 1
    return return_string

print(concat_elements(['aa','bb','cc','dd'], 1, 3))

