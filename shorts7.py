class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def __str__(self):
        return str(self._items)


def is_balanced(symbols):
    """
    Checks if the symbols are balanced

    Arguemnts:
        symbols: a string of symbols

    Returns:
        True if the symbols are balanced, False otherwise

    Precondition:
        symbols is a string of symbols from the set {'(', ')', '[', ']', '{', '}'}

    Postcondition:
        The stack is empty
    """
    stack = Stack()
    for symbol in symbols:
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                if top == "(" and symbol != ")":
                    return False
                if top == "[" and symbol != "]":
                    return False
                if top == "{" and symbol != "}":
                    return False
    return True


def decimal2binary(n):
    """
    Converts a decimal number to binary

    Arguments:
        n: a decimal number

    Returns:
        The binary representation of n

    Precondition:
        n is a non-negative integer

    Postcondition:
        The stack is empty
    """
    stack = Stack()
    while n > 0:
        stack.push(n % 2)
        n = n // 2
    result = ""
    while not stack.is_empty():
        result += str(stack.pop())
    return result


def sum_odds(arglist):
    """
    Sums the odd numbers in a list

    Arguments:
        arglist: a list of numbers

    Returns:
        The sum of the odd numbers in arglist

    Precondition:
        arglist is a list of numbers

    Postcondition:
        The list is empty
    """
    if len(arglist) == 0:
        return 0
    elif len(arglist) == 1:
        if arglist[0] % 2 == 1:
            return arglist[0]
        else:
            return 0
    else:
        if arglist[0] % 2 == 1:
            return arglist[0] + sum_odds(arglist[1:])
        else:
            return sum_odds(arglist[1:])


def count_odds(arglist):
    """
    Counts the odd numbers in a list

    Arguments:
        arglist: a list of numbers

    Returns:
        The number of odd numbers in arglist

    Precondition:
        arglist is a list of numbers

    Postcondition:
        The list is empty
    """
    if len(arglist) == 0:
        return 0
    elif len(arglist) == 1:
        if arglist[0] % 2 == 1:
            return 1
        else:
            return 0
    else:
        if arglist[0] % 2 == 1:
            return 1 + count_odds(arglist[1:])
        else:
            return count_odds(arglist[1:])