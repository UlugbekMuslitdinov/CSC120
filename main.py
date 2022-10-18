# WALRUS

# 1) a) the column n from the fkirst list is taken and the recursion comes with the rest of the list of the list
# 1) b) integer
# 2) a) the recursive part sums the first letter of string and calls the function with the rest of the string
# 2) b) string


def get_even_positions(alist):
    if len(alist) == 0:
        return []
    else:
        return [alist[0]] + get_even_positions(alist[2:])


def max_l(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return max(alist[0], max_l(alist[1:]))


def maxmin(alist):
    if len(alist) == 1:
        return alist[0], alist[0]
    else:
        max_rest, min_rest = maxmin(alist[1:])
        return max(alist[0], max_rest), min(alist[0], min_rest)


def bin_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return bin_search(alist[:mid], item)
            else:
                return bin_search(alist[mid + 1:], item)
