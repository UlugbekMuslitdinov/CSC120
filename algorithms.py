lst = [i for i in range(101)]


def binary_sort(list, item):
    low = 0
    high = len(list) - 1
    steps = 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        steps += 1

        if guess == item:
            return f"Item found {steps}"
        if item >= guess:
            low = mid + 1
        else:
            high = mid - 1

    return "Not found"


print(binary_sort(lst, 50))